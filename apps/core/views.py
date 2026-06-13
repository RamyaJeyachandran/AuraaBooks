import os
import json
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from dotenv import load_dotenv

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class GenericMasterView(TemplateView):
    template_name = 'generic_page.html'
    title = ""
    parent_name = ""
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['parent_name'] = self.parent_name
        return context

class CustomerListView(TemplateView):
    template_name = 'customers.html'

class SupplierListView(TemplateView):
    template_name = 'suppliers.html'

class ItemListView(TemplateView):
    template_name = 'items.html'

class ReferrerListView(TemplateView):
    template_name = 'referrers.html'

class WarehouseListView(TemplateView):
    template_name = 'warehouse.html'

    def get_context_data(self, **kwargs):
        from .models import Branch
        context = super().get_context_data(**kwargs)
        context['branches'] = Branch.objects.filter(is_active=True).values('id', 'name')
        return context

class PurchaseListView(TemplateView):
    template_name = 'purchases.html'

class ExpenseListView(TemplateView):
    template_name = 'expenses.html'

class AccountingView(TemplateView):
    template_name = 'accounting.html'

class BranchListView(TemplateView):
    template_name = 'branch.html'

    def get_context_data(self, **kwargs):
        from .models import Branch, EntityBankDetail, EntityShippingAddress, BranchAttachment
        import json
        context = super().get_context_data(**kwargs)
        
        branches = Branch.objects.prefetch_related('tag_accesses').order_by('id')
        branch_ids = [b.id for b in branches]
        
        # Pre-fetch banks and shipping for all branches
        all_banks = EntityBankDetail.objects.filter(entity_type='Branch', entity_id__in=branch_ids)
        all_ships = EntityShippingAddress.objects.filter(entity_type='Branch', entity_id__in=branch_ids)
        
        banks_by_branch = {}
        for bank in all_banks:
            banks_by_branch.setdefault(bank.entity_id, []).append(bank)
            
        ships_by_branch = {}
        for ship in all_ships:
            ships_by_branch.setdefault(ship.entity_id, []).append(ship)

        branch_list = []
        for b in branches:
            branch_list.append({
                'id': b.id,
                'name': b.name or '',
                'ledger_name': b.ledger_name or '',
                'contact_name': b.contact_name or '',
                'mobile': b.mobile or '',
                'work_phone': b.work_phone or '',
                'email': b.email or '',
                'gstin': b.gstin or '',
                'pan': b.pan or '',
                'is_active': b.is_active,
                'additional_info': b.additional_info or '',
                'is_msme': b.is_msme,
                'msme_type': b.msme_type or '',
                'msme_number': b.msme_number or '',
                'logo': b.logo or '',
                'attachment': b.attachment or '',
                'map_coordinates': b.map_coordinates or '',
                'created_at': b.created_at.isoformat() if b.created_at else None,
                'updated_at': b.updated_at.isoformat() if b.updated_at else None,
                'parent_branch_id': b.parent_branch_id,
                'address1': b.address1 or '',
                'address2': b.address2 or '',
                'city': b.city or '',
                'state': b.state or '',
                'country': b.country or '',
                'postal_code': b.postal_code or '',
                'bank_details': [{
                    'id': bank.id,
                    'account_name': bank.account_name or '',
                    'account_number': bank.account_number or '',
                    'account_type': bank.account_type or '',
                    'bank_name': bank.bank_name or '',
                    'branch_name': bank.branch_name or '',
                    'ifsc_code': bank.ifsc_code or '',
                    'swift_code': bank.swift_code or '',
                    'ad_code': bank.ad_code or '',
                    'correspondent_bank': bank.correspondent_bank or ''
                } for bank in banks_by_branch.get(b.id, [])],
                'shipping_addresses': [{
                    'id': ship.id,
                    'shipping_ref_name': ship.shipping_ref_name or '',
                    'shipping_gstin': ship.shipping_gstin or '',
                    'email': ship.email or '',
                    'address1': ship.address1 or '',
                    'address2': ship.address2 or '',
                    'city': ship.city or '',
                    'state': ship.state or '',
                    'country': ship.country or '',
                    'postal_code': ship.postal_code or '',
                    'mobile': ship.mobile or '',
                    'map_coordinates': ship.map_coordinates or ''
                } for ship in ships_by_branch.get(b.id, [])],
                'attachments': [{'id': att.id, 'name': att.filename, 'url': att.file.url if att.file else ''} for att in b.attachments.all()],
                'tag_accesses': [t.tag_name for t in b.tag_accesses.all()]
            })
            
        context['branch_data'] = json.dumps(branch_list)
        # Dynamic counts for dashboard
        context['total_branches'] = branches.count()
        context['active_branches'] = branches.filter(is_active=True).count()
        context['inactive_branches'] = branches.filter(is_active=False).count()
        return context

    def post(self, request, *args, **kwargs):
        from django.http import JsonResponse
        import json
        from .models import Branch, EntityBankDetail, EntityShippingAddress, BranchTagAccess, BranchAttachment
        from django.db import transaction
        import base64
        from django.core.files.base import ContentFile

        try:
            data = json.loads(request.body)
            action = data.get('action')

            if action == 'save':
                entry = data.get('data', {})
                branch_id = entry.get('id')
                
                with transaction.atomic():
                    if branch_id:
                        branch = Branch.objects.get(id=branch_id)
                        branch.name = entry.get('name')
                        branch.ledger_name = entry.get('ledger_name')
                        branch.contact_name = entry.get('contact_name')
                        branch.mobile = entry.get('mobile')
                        branch.work_phone = entry.get('work_phone')
                        branch.email = entry.get('email')
                        branch.gstin = entry.get('gstin')
                        branch.pan = entry.get('pan')
                        branch.is_active = entry.get('is_active', True)
                        branch.additional_info = entry.get('additional_info', '')
                        branch.is_msme = entry.get('is_msme', False)
                        branch.msme_type = entry.get('msme_type', '')
                        branch.msme_number = entry.get('msme_number', '')
                        
                        logo_str = entry.get('logo', '')
                        if logo_str and logo_str.startswith('data:'):
                            fmt, imgstr = logo_str.split(';base64,')
                            ext = fmt.split('/')[-1]
                            branch.logo = f"data:{fmt.split(':')[1]};base64,{imgstr}"
                        elif not logo_str:
                            branch.logo = ''
                            
                        branch.map_coordinates = entry.get('map_coordinates')
                        branch.parent_branch_id = entry.get('parent_branch_id')
                        branch.address1 = entry.get('address1')
                        branch.address2 = entry.get('address2')
                        branch.city = entry.get('city')
                        branch.state = entry.get('state')
                        branch.country = entry.get('country')
                        branch.postal_code = entry.get('postal_code')
                        branch.save()
                    else:
                        branch = Branch.objects.create(
                            name=entry.get('name'),
                            ledger_name=entry.get('ledger_name'),
                            contact_name=entry.get('contact_name'),
                            mobile=entry.get('mobile'),
                            work_phone=entry.get('work_phone'),
                            email=entry.get('email'),
                            gstin=entry.get('gstin'),
                            pan=entry.get('pan'),
                            is_active=entry.get('is_active', True),
                            additional_info=entry.get('additional_info'),
                            is_msme=entry.get('is_msme', False),
                            msme_type=entry.get('msme_type', ''),
                            msme_number=entry.get('msme_number', ''),
                            map_coordinates=entry.get('map_coordinates'),
                            parent_branch_id=entry.get('parent_branch_id'),
                            address1=entry.get('address1'),
                            address2=entry.get('address2'),
                            city=entry.get('city'),
                            state=entry.get('state'),
                            country=entry.get('country'),
                            postal_code=entry.get('postal_code')
                        )
                        
                        logo_str = entry.get('logo', '')
                        if logo_str and logo_str.startswith('data:'):
                            fmt, imgstr = logo_str.split(';base64,')
                            branch.logo = f"data:{fmt.split(':')[1]};base64,{imgstr}"
                            branch.save()
                    
                    # Update Bank Details
                    EntityBankDetail.objects.filter(entity_type='Branch', entity_id=branch.id).delete()
                    banks = entry.get('bank_details', [])
                    for bank in banks:
                        EntityBankDetail.objects.create(
                            entity_type='Branch',
                            entity_id=branch.id,
                            account_name=bank.get('account_name'),
                            account_number=bank.get('account_number'),
                            account_type=bank.get('account_type'),
                            bank_name=bank.get('bank_name'),
                            branch_name=bank.get('branch_name'),
                            ifsc_code=bank.get('ifsc_code'),
                            swift_code=bank.get('swift_code'),
                            ad_code=bank.get('ad_code'),
                            correspondent_bank=bank.get('correspondent_bank')
                        )
                        
                    # Update Shipping Address
                    EntityShippingAddress.objects.filter(entity_type='Branch', entity_id=branch.id).delete()
                    shipping = entry.get('shipping_addresses', [])
                    for ship in shipping:
                        EntityShippingAddress.objects.create(
                            entity_type='Branch',
                            entity_id=branch.id,
                            shipping_ref_name=ship.get('shipping_ref_name'),
                            shipping_gstin=ship.get('shipping_gstin'),
                            email=ship.get('email'),
                            address1=ship.get('address1'),
                            address2=ship.get('address2'),
                            city=ship.get('city'),
                            state=ship.get('state'),
                            country=ship.get('country'),
                            postal_code=ship.get('postal_code'),
                            mobile=ship.get('mobile'),
                            map_coordinates=ship.get('map_coordinates')
                        )
                        
                    # Update Tag Access
                    BranchTagAccess.objects.filter(branch=branch).delete()
                    tags = entry.get('tag_accesses', [])
                    for tag in tags:
                        if tag:
                            BranchTagAccess.objects.create(branch=branch, tag_name=tag)
                            
                    # Multiple attachments from base64
                    attach_str = entry.get('attachment', '')
                    if attach_str:
                        try:
                            attachments = json.loads(attach_str)
                            kept_ids = [att['id'] for att in attachments if 'id' in att]
                            BranchAttachment.objects.filter(branch=branch).exclude(id__in=kept_ids).delete()
                            
                            for att in attachments:
                                if 'data' in att and att['data'].startswith('data:'):
                                    fmt, imgstr = att['data'].split(';base64,')
                                    ext = fmt.split('/')[-1]
                                    filename = att.get('name', f'attachment.{ext}')
                                    BranchAttachment.objects.create(
                                        branch=branch,
                                        file=ContentFile(base64.b64decode(imgstr), name=filename),
                                        filename=filename
                                    )
                        except:
                            pass
                    else:
                        BranchAttachment.objects.filter(branch=branch).delete()

                    
                    branch_data = {
                        'id': branch.id,
                        'name': branch.name or '',
                        'ledger_name': branch.ledger_name or '',
                        'contact_name': branch.contact_name or '',
                        'mobile': branch.mobile or '',
                        'work_phone': branch.work_phone or '',
                        'email': branch.email or '',
                        'gstin': branch.gstin or '',
                        'pan': branch.pan or '',
                        'is_active': branch.is_active,
                        'additional_info': branch.additional_info or '',
                        'is_msme': branch.is_msme,
                        'msme_type': branch.msme_type or '',
                        'msme_number': branch.msme_number or '',
                        'logo': branch.logo or '',
                        'attachment': branch.attachment or '',
                        'map_coordinates': branch.map_coordinates or '',
                        'parent_branch_id': branch.parent_branch_id,
                        'address1': branch.address1 or '',
                        'address2': branch.address2 or '',
                        'city': branch.city or '',
                        'state': branch.state or '',
                        'country': branch.country or '',
                        'postal_code': branch.postal_code or '',
                        'bank_details': [{
                            'id': bank.id,
                            'account_name': bank.account_name or '',
                            'account_number': bank.account_number or '',
                            'account_type': bank.account_type or '',
                            'bank_name': bank.bank_name or '',
                            'branch_name': bank.branch_name or '',
                            'ifsc_code': bank.ifsc_code or '',
                            'swift_code': bank.swift_code or '',
                            'ad_code': bank.ad_code or '',
                            'correspondent_bank': bank.correspondent_bank or ''
                        } for bank in EntityBankDetail.objects.filter(entity_type='Branch', entity_id=branch.id)],
                        'shipping_addresses': [{
                            'id': ship.id,
                            'shipping_ref_name': ship.shipping_ref_name or '',
                            'shipping_gstin': ship.shipping_gstin or '',
                            'email': ship.email or '',
                            'address1': ship.address1 or '',
                            'address2': ship.address2 or '',
                            'city': ship.city or '',
                            'state': ship.state or '',
                            'country': ship.country or '',
                            'postal_code': ship.postal_code or '',
                            'mobile': ship.mobile or '',
                            'map_coordinates': ship.map_coordinates or ''
                        } for ship in EntityShippingAddress.objects.filter(entity_type='Branch', entity_id=branch.id)],
                        'attachments': [{'id': att.id, 'name': att.filename, 'url': att.file.url if att.file else ''} for att in branch.attachments.all()],
                        'tag_accesses': [t.tag_name for t in branch.tag_accesses.all()]
                    }
                return JsonResponse({'status': 'success', 'message': 'Branch saved successfully.', 'branch': branch_data})

            elif action == 'delete':
                branch_id = data.get('id')
                if branch_id:
                    Branch.objects.filter(id=branch_id).delete()
                    EntityBankDetail.objects.filter(entity_type='Branch', entity_id=branch_id).delete()
                    EntityShippingAddress.objects.filter(entity_type='Branch', entity_id=branch_id).delete()
                    BranchAttachment.objects.filter(branch_id=branch_id).delete()
                    return JsonResponse({'status': 'success', 'message': 'Branch deleted successfully.'})
                return JsonResponse({'status': 'error', 'message': 'Invalid branch ID.'}, status=400)

            return JsonResponse({'status': 'error', 'message': 'Invalid action.'}, status=400)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

class TagView(View):
    def get(self, request):
        from .models import Tag, BranchTagAccess
        from django.db.models import Count
        tags = Tag.objects.all().order_by('name')
        
        tag_list = []
        for tag in tags:
            # Count branches that use this tag_name
            count = BranchTagAccess.objects.filter(tag_name=tag.name).count()
            tag_list.append({
                'id': tag.id,
                'name': tag.name,
                'count': count
            })
            
        return JsonResponse({'status': 'success', 'tags': tag_list})

    def post(self, request):
        import json
        from .models import Tag
        try:
            data = json.loads(request.body)
            name = data.get('name')
            if not name:
                return JsonResponse({'status': 'error', 'message': 'Tag name is required.'}, status=400)
                
            tag, created = Tag.objects.get_or_create(name=name)
            return JsonResponse({'status': 'success', 'message': 'Tag added successfully.', 'tag': {'id': tag.id, 'name': tag.name, 'count': 0}})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    def put(self, request):
        import json
        from .models import Tag, BranchTagAccess
        try:
            data = json.loads(request.body)
            tag_id = data.get('id')
            new_name = data.get('name')
            
            if not tag_id or not new_name:
                return JsonResponse({'status': 'error', 'message': 'Tag ID and new name are required.'}, status=400)
                
            tag = Tag.objects.filter(id=tag_id).first()
            if not tag:
                return JsonResponse({'status': 'error', 'message': 'Tag not found.'}, status=404)
                
            old_name = tag.name
            tag.name = new_name
            tag.save()
            
            # Update all associated BranchTagAccess records
            if old_name != new_name:
                BranchTagAccess.objects.filter(tag_name=old_name).update(tag_name=new_name)
                
            return JsonResponse({'status': 'success', 'message': 'Tag updated successfully.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    def delete(self, request):
        import json
        from .models import Tag, BranchTagAccess
        try:
            data = json.loads(request.body)
            tag_id = data.get('id')
            if not tag_id:
                return JsonResponse({'status': 'error', 'message': 'Tag ID is required.'}, status=400)
                
            tag = Tag.objects.filter(id=tag_id).first()
            if tag:
                # Also optionally unlink it from BranchTagAccess
                BranchTagAccess.objects.filter(tag_name=tag.name).delete()
                tag.delete()
                return JsonResponse({'status': 'success', 'message': 'Tag deleted successfully.'})
            return JsonResponse({'status': 'error', 'message': 'Tag not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

class FranchiseeListView(TemplateView):
    template_name = 'franchisee.html'

    def get_context_data(self, **kwargs):
        from .models import Branch, Franchisee, Tag, EntityShippingAddress
        import json
        context = super().get_context_data(**kwargs)
        
        franchisees = Franchisee.objects.prefetch_related('tag_accesses', 'attachments').order_by('id')
        context['franchisees'] = franchisees
        context['total_franchisees'] = franchisees.count()
        context['active_franchisees'] = sum(1 for f in franchisees if f.is_active)
        context['inactive_franchisees'] = context['total_franchisees'] - context['active_franchisees']
        context['branches'] = Branch.objects.all()
        context['tags'] = Tag.objects.filter(tag_type='B')
        
        franchisee_list = []
        for f in franchisees:
            franchisee_list.append({
                'id': f.id,
                'name': f.name or '',
                'contact_name': f.contact_name or '',
                'ledger_name': f.ledger_name or '',
                'mobile': f.mobile or '',
                'work_phone': f.work_phone or '',
                'email': f.email or '',
                'gstin': f.gstin or '',
                'pan': f.pan or '',
                'commission': str(f.commission_percent) if f.commission_percent else '',
                'is_active': f.is_active,
                'is_composition_scheme': f.is_composition_scheme,
                'is_msme': f.is_msme,
                'msme_type': getattr(f, 'msme_type', '') or '',
                'msme_number': getattr(f, 'msme_number', '') or '',
                # Billing Address
                'address1': f.address1 or '',
                'address2': f.address2 or '',
                'city': f.city or '',
                'state': f.state or '',
                'country': f.country or 'India',
                'postal_code': f.postal_code or '',
                # Shipping Address
                'same_as_billing': f.same_as_billing,
                'shipping_addresses': [
                    {
                        'shipping_ref_name': ship.shipping_ref_name or '',
                        'shipping_gstin': ship.shipping_gstin or '',
                        'shipping_address1': ship.address1 or '',
                        'shipping_address2': ship.address2 or '',
                        'shipping_city': ship.city or '',
                        'shipping_state': ship.state or '',
                        'shipping_country': ship.country or 'India',
                        'shipping_postal_code': ship.postal_code or '',
                        'shipping_phone': ship.mobile or '',
                        'shipping_email': ship.email or '',
                        'shipping_latitude': ship.map_coordinates.split(',')[0].strip() if ship.map_coordinates and ',' in ship.map_coordinates else '',
                        'shipping_longitude': ship.map_coordinates.split(',')[1].strip() if ship.map_coordinates and ',' in ship.map_coordinates else '',
                    }
                    for ship in EntityShippingAddress.objects.filter(entity_type='Franchisee', entity_id=f.id)
                ],
                # Billing lat/lng
                'latitude': f.latitude or '',
                'longitude': f.longitude or '',
                # Bank Details
                'account_name': f.account_name or '',
                'account_number': f.account_number or '',
                'account_type': f.account_type or '',
                'bank_name': f.bank_name or '',
                'bank_branch': f.bank_branch or '',
                'ifsc_code': f.ifsc_code or '',
                'swift_code': f.swift_code or '',
                'ad_code': f.dealer_code or '',
                'correspondent_bank': f.correspondent_bank or '',
                # Branch
                'assign_under_branch': f.assign_under_branch,
                'branch_id': f.branch_id,
                'tag_accesses': [t.tag_name for t in f.tag_accesses.all()],
                'attachments': [{'id': a.id, 'name': a.filename, 'data': a.file.url} for a in f.attachments.all() if a.file]
            })
        
        context['franchisee_data'] = json.dumps(franchisee_list)
        return context

    def post(self, request, *args, **kwargs):
        from .models import Franchisee, Branch, FranchiseeTagAccess, FranchiseeAttachment
        import json
        import base64
        from django.core.files.base import ContentFile
        try:
            data = json.loads(request.body)
            action = data.get('action')
            
            if action == 'save':
                f_data = data.get('data', {})
                f_id = f_data.get('id')
                
                # Main fields
                franchisee_dict = {
                    'name': f_data.get('name', ''),
                    'contact_name': f_data.get('contact_name', ''),
                    'ledger_name': f_data.get('ledger_name', ''),
                    'gstin': f_data.get('gstin', ''),
                    'pan': f_data.get('pan', ''),
                    'is_msme': f_data.get('is_msme', False),
                    'is_composition_scheme': f_data.get('is_composition_scheme', False),
                    'mobile': f_data.get('mobile', ''),
                    'work_phone': f_data.get('work_phone', ''),
                    'email': f_data.get('email', ''),
                    'is_active': f_data.get('is_active', True),
                    'commission_percent': f_data.get('commission') or 0,
                    
                    'address1': f_data.get('address1', ''),
                    'address2': f_data.get('address2', ''),
                    'city': f_data.get('city', ''),
                    'postal_code': f_data.get('postal_code', ''),
                    'country': f_data.get('country', 'India'),
                    'state': f_data.get('state', ''),
                    'latitude': f_data.get('latitude', ''),
                    'longitude': f_data.get('longitude', ''),
                    
                    'same_as_billing': f_data.get('same_as_billing', False),
                    
                    'assign_under_branch': f_data.get('assign_under_branch', False)
                }
                
                # Bank details
                bank_details = f_data.get('bank_details', [])
                if bank_details and len(bank_details) > 0:
                    bd = bank_details[0]
                    franchisee_dict['account_name'] = bd.get('account_name', '')
                    franchisee_dict['account_number'] = bd.get('account_number', '')
                    franchisee_dict['account_type'] = bd.get('account_type', '')
                    franchisee_dict['bank_name'] = bd.get('bank_name', '')
                    franchisee_dict['bank_branch'] = bd.get('bank_branch', '')
                    franchisee_dict['ifsc_code'] = bd.get('ifsc_code', '')
                    franchisee_dict['swift_code'] = bd.get('swift_code', '')
                    franchisee_dict['dealer_code'] = bd.get('ad_code', '')
                    franchisee_dict['correspondent_bank'] = bd.get('correspondent_bank', '')
                
                branch_id = f_data.get('branch_id')
                if branch_id and franchisee_dict['assign_under_branch']:
                    franchisee_dict['branch_id'] = branch_id
                else:
                    franchisee_dict['branch_id'] = None
                
                if f_id:
                    Franchisee.objects.filter(id=f_id).update(**franchisee_dict)
                    franchisee = Franchisee.objects.get(id=f_id)
                else:
                    franchisee = Franchisee.objects.create(**franchisee_dict)
                
                # Shipping addresses
                from .models import EntityShippingAddress
                EntityShippingAddress.objects.filter(entity_type='Franchisee', entity_id=franchisee.id).delete()
                shipping_addresses = f_data.get('shipping_addresses', [])
                for ship in shipping_addresses:
                    map_coords = ''
                    if ship.get('shipping_latitude') and ship.get('shipping_longitude'):
                        map_coords = f"{ship.get('shipping_latitude')}, {ship.get('shipping_longitude')}"
                        
                    EntityShippingAddress.objects.create(
                        entity_type='Franchisee',
                        entity_id=franchisee.id,
                        shipping_ref_name=ship.get('shipping_ref_name', ''),
                        shipping_gstin=ship.get('shipping_gstin', ''),
                        address1=ship.get('shipping_address1', ''),
                        address2=ship.get('shipping_address2', ''),
                        city=ship.get('shipping_city', ''),
                        postal_code=ship.get('shipping_postal_code', ''),
                        country=ship.get('shipping_country', 'India'),
                        state=ship.get('shipping_state', ''),
                        mobile=ship.get('shipping_phone', ''),
                        email=ship.get('shipping_email', ''),
                        map_coordinates=map_coords
                    )
                
                # Tags
                tags_list = f_data.get('tag_accesses', [])
                FranchiseeTagAccess.objects.filter(franchisee=franchisee).delete()
                for t in tags_list:
                    FranchiseeTagAccess.objects.create(franchisee=franchisee, tag_name=t)
                
                # Multiple attachments from base64
                attach_str = f_data.get('attachment', '')
                if attach_str:
                    try:
                        attachments = json.loads(attach_str)
                        kept_ids = [att['id'] for att in attachments if 'id' in att]
                        FranchiseeAttachment.objects.filter(franchisee=franchisee).exclude(id__in=kept_ids).delete()
                        
                        for att in attachments:
                            if 'data' in att and att['data'].startswith('data:'):
                                fmt, imgstr = att['data'].split(';base64,')
                                ext = fmt.split('/')[-1]
                                filename = att.get('name', f'attachment.{ext}')
                                FranchiseeAttachment.objects.create(
                                    franchisee=franchisee,
                                    file=ContentFile(base64.b64decode(imgstr), name=filename),
                                    filename=filename
                                )
                    except:
                        pass
                else:
                    FranchiseeAttachment.objects.filter(franchisee=franchisee).delete()
                
                # Construct response data
                franchisee_res = {
                    'id': franchisee.id,
                    'name': franchisee.name,
                    'contact_name': franchisee.contact_name,
                    'ledger_name': franchisee.ledger_name,
                    'mobile': franchisee.mobile,
                    'city': franchisee.city,
                    'is_active': franchisee.is_active,
                    'is_composition_scheme': franchisee.is_composition_scheme,
                    'is_msme': franchisee.is_msme,
                    'gstin': franchisee.gstin,
                    'pan': franchisee.pan,
                    'email': franchisee.email,
                    'work_phone': franchisee.work_phone,
                    'address1': franchisee.address1,
                    'address2': franchisee.address2,
                    'state': franchisee.state,
                    'country': franchisee.country,
                    'postal_code': franchisee.postal_code,
                    'assign_under_branch': franchisee.assign_under_branch,
                    'branch_id': franchisee.branch_id,
                    'tag_accesses': [t.tag_name for t in franchisee.tag_accesses.all()],
                    'attachments': [{'id': a.id, 'name': a.filename, 'data': a.file.url} for a in franchisee.attachments.all() if a.file]
                }
                
                return JsonResponse({'status': 'success', 'message': 'Franchisee saved successfully.', 'franchisee': franchisee_res})
                
            elif action == 'delete':
                f_id = data.get('id')
                if f_id:
                    Franchisee.objects.filter(id=f_id).delete()
                    return JsonResponse({'status': 'success', 'message': 'Franchisee deleted successfully.'})
                return JsonResponse({'status': 'error', 'message': 'Invalid ID.'}, status=400)
                
        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

class ProjectListView(TemplateView):
    template_name = 'project.html'

class SalesRepListView(TemplateView):
    template_name = 'sales_rep.html'

class BankCashListView(TemplateView):
    template_name = 'banks_cash.html'

class RateSheetListView(TemplateView):
    template_name = 'rate_sheet.html'

class StockJournalListView(TemplateView):
    template_name = 'stock_journal.html'
class CreditExpenseListView(TemplateView):
    template_name = 'expenses_credit.html'

class AssetExpenseListView(TemplateView):
    template_name = 'expenses_asset.html'

class CashExpenseListView(TemplateView):
    template_name = 'expenses_cash.html'

class ReclaimExpenseListView(TemplateView):
    template_name = 'expenses_reclaim.html'

class DeliveryChallanListView(TemplateView):
    template_name = 'sales_delivery_challan.html'

class CreditNoteListView(TemplateView):
    template_name = 'sales_credit_note.html'

class ReceiptListView(TemplateView):
    template_name = 'sales_receipt.html'


class SalesQuotesListView(TemplateView):
    template_name = 'sales_quotes.html'

    def get_context_data(self, **kwargs):
        from .models import PremiumQuote, Customer
        context = super().get_context_data(**kwargs)
        context['premium_quotes'] = PremiumQuote.objects.all().order_by('-id')
        context['customers'] = Customer.objects.all()
        return context


class SalesOrdersListView(TemplateView):
    template_name = 'sales_orders.html'


class SalesInvoicesListView(TemplateView):
    template_name = 'sales_invoices.html'


class PurchaseQuotesListView(TemplateView):
    template_name = 'purchase_quotes.html'

class PurchaseOrdersListView(TemplateView):
    template_name = 'purchase_orders.html'

class SupplierCreditNoteListView(TemplateView):
    template_name = 'supplier_credit_note.html'

class GoodsReceiptListView(TemplateView):
    template_name = 'goods_receipt.html'

class PurchaseBillView(TemplateView):
    template_name = 'purchase_bill.html'

class PurchasePaymentView(TemplateView):
    template_name = 'purchase_payment.html'


class AccountsListView(TemplateView):
    template_name = 'accounts.html'


class OpeningBalanceListView(TemplateView):
    template_name = 'opening_balance.html'


class SettingsDashboardView(TemplateView):
    template_name = 'settings_dashboard.html'


@method_decorator(csrf_exempt, name='dispatch')
class SmtpSettingsView(TemplateView):
    template_name = 'smtp_settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import SmtpSettings
        cid = self.request.session.get('cid', '1')
        settings, _ = SmtpSettings.objects.get_or_create(cid=cid, type='E')
        
        # Default empty config if settings.settings is None
        default_config = {
            'host': '',
            'connection': 'None',
            'port': '25',
            'email': '',
            'password': '',
            'fromName': '',
            'fromEmail': ''
        }
        
        if settings.settings:
            try:
                db_config = json.loads(settings.settings)
                # Map db_config to frontend format
                default_config = {
                    'host': db_config.get('smtp_host', ''),
                    'connection': db_config.get('smtp_crypto', 'None'),
                    'port': db_config.get('smtp_port', '25'),
                    'email': db_config.get('smtp_user', ''),
                    'password': db_config.get('smtp_pass', ''),
                    'fromName': db_config.get('smtp_from_name', ''),
                    'fromEmail': db_config.get('smtp_from', '')
                }
            except json.JSONDecodeError:
                pass
                
        context['smtp_config'] = json.dumps(default_config)
        return context

    def post(self, request, *args, **kwargs):
        import smtplib
        from email.mime.text import MIMEText
        from .models import SmtpSettings
        
        try:
            data = json.loads(request.body)
            action = data.get('action')
            cid = request.session.get('cid', '1')
            
            smtp_data = data.get('data', {})
            host = smtp_data.get('host', '')
            connection_type = smtp_data.get('connection', 'None')
            port = int(smtp_data.get('port', 25) or 25)
            user = smtp_data.get('email', '')
            password = smtp_data.get('password', '')
            from_name = smtp_data.get('fromName', '')
            from_email = smtp_data.get('fromEmail', '')
            
            if action == 'save':
                db_config = {
                    'smtp_host': host,
                    'smtp_crypto': connection_type,
                    'smtp_port': str(port),
                    'smtp_user': user,
                    'smtp_pass': password,
                    'smtp_from_name': from_name,
                    'smtp_from': from_email
                }
                settings, _ = SmtpSettings.objects.get_or_create(cid=cid, type='E')
                settings.settings = json.dumps(db_config)
                settings.save()
                return JsonResponse({'status': 'success', 'message': 'SMTP settings saved successfully'})
                
            elif action == 'test':
                msg = MIMEText('This is a test email to verify SMTP settings.')
                msg['Subject'] = 'SMTP Configuration Test'
                msg['From'] = f"{from_name} <{from_email}>" if from_name else from_email
                msg['To'] = user or from_email
                
                try:
                    server = smtplib.SMTP(host, port, timeout=10)
                    if connection_type.lower() == 'tls':
                        server.starttls()
                    elif connection_type.lower() == 'ssl':
                        server = smtplib.SMTP_SSL(host, port, timeout=10)
                        
                    if user and password:
                        server.login(user, password)
                        
                    server.send_message(msg)
                    server.quit()
                    return JsonResponse({'status': 'success', 'message': 'Test email sent successfully!'})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': f'SMTP Connection failed: {str(e)}'})

            return JsonResponse({'status': 'error', 'message': 'Invalid action'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class StorageLocationView(TemplateView):
    template_name = 'storage_location.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import StorageLocation
        cid = self.request.session.get('cid', '1')
        
        storages = StorageLocation.objects.filter(cid=cid).order_by('id')
        storage_list = []
        for s in storages:
            storage_list.append({
                'id': s.id,
                'code': s.code,
                'name': s.name,
                'from': s.range_from or '',
                'to': s.range_to or ''
            })
            
        context['storage_data'] = json.dumps(storage_list)
        return context

    def post(self, request, *args, **kwargs):
        from .models import StorageLocation
        try:
            data = json.loads(request.body)
            action = data.get('action')
            cid = request.session.get('cid', '1')
            
            if action == 'save':
                sto_data = data.get('data', {})
                sto_id = sto_data.get('id')
                
                if sto_id:
                    try:
                        storage = StorageLocation.objects.get(id=sto_id, cid=cid)
                        storage.code = sto_data.get('code')
                        storage.name = sto_data.get('name')
                        storage.range_from = sto_data.get('from', '')
                        storage.range_to = sto_data.get('to', '')
                        storage.save()
                    except StorageLocation.DoesNotExist:
                        return JsonResponse({'status': 'error', 'message': 'Storage location not found'})
                else:
                    StorageLocation.objects.create(
                        cid=cid,
                        code=sto_data.get('code'),
                        name=sto_data.get('name'),
                        range_from=sto_data.get('from', ''),
                        range_to=sto_data.get('to', '')
                    )
                return JsonResponse({'status': 'success', 'message': 'Storage location saved successfully'})
                
            elif action == 'delete':
                sto_id = data.get('id')
                if sto_id:
                    StorageLocation.objects.filter(id=sto_id, cid=cid).delete()
                    return JsonResponse({'status': 'success', 'message': 'Storage location deleted successfully'})
                return JsonResponse({'status': 'error', 'message': 'ID not provided for deletion'})

            return JsonResponse({'status': 'error', 'message': 'Invalid action'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

class CustomerPointsSettingsView(TemplateView):
    template_name = 'customer_points_settings.html'


class QrCodeSettingsView(TemplateView):
    template_name = 'qr_code_settings.html'


class UnitsSettingsView(TemplateView):
    template_name = 'units_settings.html'

    def get_context_data(self, **kwargs):
        from .models import Unit
        import json
        context = super().get_context_data(**kwargs)
        cid = self.request.session.get('companyId', 1)
        units = list(Unit.objects.filter(companyId=cid).values(
            'id', 'name', 'code', 'descr', 'convFactor', 'isActive', 'isDefault', 'relatedUnits'
        ).order_by('name'))
        
        # Convert Decimals to string for JSON serialization
        for u in units:
            if u['convFactor'] is not None:
                u['convFactor'] = float(u['convFactor'])
            else:
                u['convFactor'] = 1.0
                
            if u['relatedUnits'] is None:
                u['relatedUnits'] = []
                
        context['units_data'] = json.dumps(units)
        return context

    def post(self, request, *args, **kwargs):
        from .models import Unit
        import json
        try:
            data = json.loads(request.body)
            action = data.get('action')
            cid = request.session.get('companyId', 1)

            if action == 'save_unit':
                u_id = data.get('id')
                name = data.get('name', '')
                code = data.get('code', '')
                descr = data.get('descr', '')
                is_active = data.get('isActive', True)
                is_default = data.get('isDefault', False)
                related_units = data.get('relatedUnits', [])

                # Enforce unique name per company
                if Unit.objects.filter(companyId=cid, name__iexact=name).exclude(id=u_id).exists():
                    return JsonResponse({'status': 'error', 'message': f'Unit name "{name}" already exists for this company.'})

                if is_default:
                    # If this is set to default, unset others in this company
                    Unit.objects.filter(companyId=cid, isDefault=True).update(isDefault=False)

                if u_id:
                    unit = Unit.objects.get(id=u_id, companyId=cid)
                    unit.name = name
                    unit.code = code
                    unit.descr = descr
                    unit.isActive = is_active
                    unit.isDefault = is_default
                    unit.relatedUnits = related_units
                    unit.save()
                    msg = 'Unit updated successfully.'
                else:
                    unit = Unit.objects.create(
                        companyId=cid,
                        name=name,
                        code=code,
                        descr=descr,
                        isActive=is_active,
                        isDefault=is_default,
                        relatedUnits=related_units,
                        convFactor=1.0 # Default factor for the unit itself
                    )
                    msg = 'Unit created successfully.'

                return JsonResponse({'status': 'success', 'message': msg})

            elif action == 'delete_unit':
                u_id = data.get('id')
                try:
                    Unit.objects.filter(id=u_id).delete()
                    return JsonResponse({'status': 'success', 'message': 'Unit deleted successfully.'})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': f'Cannot delete unit: {str(e)}'})

            return JsonResponse({'status': 'error', 'message': 'Invalid action'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


class PrintSettingsView(TemplateView):
    template_name = 'print_settings.html'


@method_decorator(csrf_exempt, name='dispatch')
class ModulesSettingsView(TemplateView):
    template_name = 'modules_settings.html'

    def get_context_data(self, **kwargs):
        from .models import Module
        context = super().get_context_data(**kwargs)
        # Fetch parents first
        parents = Module.objects.filter(parent__isnull=True).order_by('display_order')
        # Group children manually to avoid multiple queries or we can just fetch all
        modules = []
        all_modules = Module.objects.all().order_by('display_order')
        for p in parents:
            children = [c for c in all_modules if c.parent_id == p.id]
            if not children:
                # If no submenus, show the menu itself
                modules.append(p)
            else:
                # If it has submenus, only show the submenus
                for c in children:
                    modules.append(c)
        context['modules_list'] = modules
        return context

    def post(self, request, *args, **kwargs):
        from .models import Module
        try:
            data = json.loads(request.body)
            action = data.get('action')

            if action == 'toggle_status':
                module_id = data.get('module_id')
                is_active = data.get('is_active')
                module = Module.objects.get(id=module_id)
                module.is_active = is_active
                module.save()
                return JsonResponse({'status': 'success', 'message': 'Module status updated'})
                
            elif action == 'edit_module':
                module_id = data.get('module_id')
                module_name = data.get('module_name')
                route_path = data.get('route_path')
                icon_name = data.get('icon_name')
                module = Module.objects.get(id=module_id)
                if module_name:
                    module.module_name = module_name
                if route_path is not None:
                    module.route_path = route_path
                if icon_name is not None:
                    module.icon_name = icon_name
                module.save()
                return JsonResponse({'status': 'success', 'message': 'Module updated successfully'})

            return JsonResponse({'status': 'error', 'message': 'Invalid action'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


@method_decorator(csrf_exempt, name='dispatch')
class SerialNumbersView(TemplateView):
    template_name = 'serial_numbers_settings.html'

    def get_context_data(self, **kwargs):
        from .models import DocumentSequence
        context = super().get_context_data(**kwargs)
        load_dotenv()
        cid = os.environ.get('CID')
        # Fetch sequences for the current CID
        sequences = DocumentSequence.objects.filter(cid=cid).order_by('id')
        seq_list = []
        for seq in sequences:
            seq_list.append({
                'id': seq.id,
                'module': seq.module,
                'series': seq.series_name,
                'mode': seq.mode,
                'prefix': seq.prefix if seq.prefix else '',
                'next': seq.next_number,
                'suffix': seq.suffix if seq.suffix else '',
                'isDefault': seq.is_default
            })
        
        context['serialData'] = json.dumps(seq_list)
        return context

    def post(self, request, *args, **kwargs):
        from .models import DocumentSequence
        try:
            data = json.loads(request.body)
            load_dotenv()
            cid = os.environ.get('CID')
            
            serial_data = data.get('serialData', [])
            
            # Since rows can be deleted or added, the easiest approach is to update existing by ID,
            # create new ones, and delete removed ones. But wait, new ones have generated IDs from JS.
            # So a simpler way for settings is to wipe and replace, or carefully sync.
            # Let's wipe and replace for this specific CID to ensure exact sync with the UI.
            
            DocumentSequence.objects.filter(cid=cid).delete()
            
            new_sequences = []
            for row in serial_data:
                new_sequences.append(DocumentSequence(
                    module=row.get('module'),
                    series_name=row.get('series'),
                    mode=row.get('mode', 'Auto'),
                    prefix=row.get('prefix', ''),
                    next_number=row.get('next', 1),
                    suffix=row.get('suffix', ''),
                    is_default=row.get('isDefault', False),
                    cid=cid
                ))
            
            DocumentSequence.objects.bulk_create(new_sequences)
            
            return JsonResponse({'status': 'success', 'message': 'Serial configurations saved successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


@method_decorator(csrf_exempt, name='dispatch')
class CompanySettingsView(TemplateView):
    template_name = 'company_settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        load_dotenv()
        cid = os.environ.get('CID')
        company_data = {}
        if cid:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT c.id, c.name, c.address1, c.address2,
                           c."mobileNo", c."emailId", c."appColorCode",
                           d."registrationNo", d."taxId", d.website, d.notes,
                           d.city, d.state, d.country, d.postal_code, d.business_type, d.timezone
                    FROM public.tbl_company c
                    LEFT JOIN public.tbl_company_details d ON c.id = d."companyId"
                    WHERE c.code = %s
                """, [cid])
                row = cursor.fetchone()
                if row:
                    col_names = [desc[0] for desc in cursor.description]
                    company_data = dict(zip(col_names, row))
        context['company'] = company_data
        return context

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            load_dotenv()
            cid = os.environ.get('CID')
            if not cid:
                return JsonResponse({'status': 'error', 'message': 'CID not set in environment.'})
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id FROM public.tbl_company WHERE code = %s", [cid])
                row = cursor.fetchone()
                if not row:
                    return JsonResponse({'status': 'error', 'message': 'Company not found.'})
                
                company_id = row[0]
                
                if 'name' in data:
                    cursor.execute("""
                        UPDATE public.tbl_company
                        SET name = %s, address1 = %s, address2 = %s,
                            "mobileNo" = %s, "emailId" = %s
                        WHERE id = %s
                    """, [
                        data.get('name'), data.get('address1'), data.get('address2'),
                        data.get('phone'), data.get('email'), company_id
                    ])
                    
                    cursor.execute("SELECT id FROM public.tbl_company_details WHERE \"companyId\" = %s", [company_id])
                    detail_row = cursor.fetchone()
                    if detail_row:
                        cursor.execute("""
                            UPDATE public.tbl_company_details
                            SET notes = %s, city = %s, state = %s, country = %s, postal_code = %s,
                                business_type = %s, timezone = %s
                            WHERE "companyId" = %s
                        """, [
                            data.get('notes'), data.get('city'), data.get('state'), data.get('country'),
                            data.get('postal_code'), data.get('business_type'), data.get('timezone'),
                            company_id
                        ])
                    else:
                        cursor.execute("""
                            INSERT INTO public.tbl_company_details (
                                "companyId", notes, city, state, country, postal_code, business_type, timezone
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """, [
                            company_id, data.get('notes'), data.get('city'), data.get('state'), data.get('country'),
                            data.get('postal_code'), data.get('business_type'), data.get('timezone')
                        ])
                        
                if 'taxId' in data:
                    cursor.execute("SELECT id FROM public.tbl_company_details WHERE \"companyId\" = %s", [company_id])
                    detail_row = cursor.fetchone()
                    if detail_row:
                        cursor.execute("""
                            UPDATE public.tbl_company_details
                            SET "taxId" = %s, "registrationNo" = %s
                            WHERE "companyId" = %s
                        """, [
                            data.get('taxId'), data.get('pan'), company_id
                        ])
                    else:
                        cursor.execute("""
                            INSERT INTO public.tbl_company_details (
                                "companyId", "taxId", "registrationNo"
                            ) VALUES (%s, %s, %s)
                        """, [
                            company_id, data.get('taxId'), data.get('pan')
                        ])
                    
            return JsonResponse({'status': 'success', 'message': 'Company details updated.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


@method_decorator(csrf_exempt, name='dispatch')
class DefaultContentView(TemplateView):
    template_name = 'default_content_settings.html'

    def get_context_data(self, **kwargs):
        from .models import DefaultContent
        context = super().get_context_data(**kwargs)
        load_dotenv()
        cid = os.environ.get('CID')
        # Filter by branch if needed, currently assuming global default per company/branch or just fetching all
        contents = DefaultContent.objects.all()
        
        content_list = []
        for c in contents:
            content_list.append({
                'name': c.document_type,
                'subType': c.sub_type or '',
                'notes': c.notes or '',
                'terms': c.terms or '',
                'emailCC': c.email_cc or '',
                'emailSubject': c.email_subject or '',
                'emailContent': c.email_content or '',
                'smsMsgId': c.sms_msg_id or '',
                'smsContent': c.sms_content or '',
                'whatsappMsgId': c.whatsapp_msg_id or '',
                'whatsappContent': c.whatsapp_content or ''
            })
        context['defaultContentData'] = json.dumps(content_list)
        return context

    def post(self, request, *args, **kwargs):
        from .models import DefaultContent
        try:
            data = json.loads(request.body)
            doc_type = data.get('name')
            sub_type = data.get('subType', '')
            
            content, created = DefaultContent.objects.get_or_create(
                document_type=doc_type,
                sub_type=sub_type,
                defaults={
                    'notes': data.get('notes', ''),
                    'terms': data.get('terms', ''),
                    'email_cc': data.get('emailCC', ''),
                    'email_subject': data.get('emailSubject', ''),
                    'email_content': data.get('emailContent', ''),
                    'sms_msg_id': data.get('smsMsgId', ''),
                    'sms_content': data.get('smsContent', ''),
                    'whatsapp_msg_id': data.get('whatsappMsgId', ''),
                    'whatsapp_content': data.get('whatsappContent', '')
                }
            )
            if not created:
                content.notes = data.get('notes', '')
                content.terms = data.get('terms', '')
                content.email_cc = data.get('emailCC', '')
                content.email_subject = data.get('emailSubject', '')
                content.email_content = data.get('emailContent', '')
                content.sms_msg_id = data.get('smsMsgId', '')
                content.sms_content = data.get('smsContent', '')
                content.whatsapp_msg_id = data.get('whatsappMsgId', '')
                content.whatsapp_content = data.get('whatsappContent', '')
                content.save()
            
            return JsonResponse({'status': 'success', 'message': 'Default content saved successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


class TaxRatesSettingsView(TemplateView):
    template_name = 'tax_rates_settings.html'


@method_decorator(csrf_exempt, name='dispatch')
class CustomFieldsView(TemplateView):
    template_name = 'custom_fields_settings.html'

    def get_context_data(self, **kwargs):
        from .models import CustomField, Module
        context = super().get_context_data(**kwargs)
        load_dotenv()
        cid = os.environ.get('CID')
        fields = CustomField.objects.filter(cid=cid).select_related('module').order_by('id')
        
        fields_list = []
        for field in fields:
            fields_list.append({
                'id': field.id,
                'name': field.name,
                'moduleId': field.module.id if field.module else '',
                'moduleName': field.module.module_name if field.module else '',
                'fieldType': field.field_type,
                'defaultVal': field.default_value if field.default_value else '',
                'itemGrid': field.is_item_grid,
                'includeTotal': field.include_total,
                'required': field.is_required,
                'displayInPrint': field.display_in_print,
                'subtypes': json.loads(field.subtypes) if field.subtypes else ['All'],
                'active': field.is_active
            })
            
        context['customFieldsData'] = json.dumps(fields_list)
        
        excluded_modules = ['Dashboard', 'E-Commerce', 'Enhanced Export/Import', 'Settings', 'Accounting']
        available_modules = list(Module.objects.filter(is_active=True).exclude(module_name__in=excluded_modules).values('id', 'module_name').order_by('module_name'))
        context['available_modules'] = available_modules
        
        return context

    def post(self, request, *args, **kwargs):
        from .models import CustomField
        try:
            data = json.loads(request.body)
            load_dotenv()
            cid = os.environ.get('CID')
            
            action = data.get('action')
            
            if action == 'save':
                field_data = data.get('fieldData', {})
                field_id = field_data.get('id')
                subtypes_json = json.dumps(field_data.get('subtypes', ['All']))
                
                if field_id:
                    try:
                        field = CustomField.objects.get(id=field_id, cid=cid)
                        field.name = field_data.get('name')
                        field.module_id = field_data.get('moduleId')
                        field.field_type = field_data.get('fieldType')
                        field.default_value = field_data.get('defaultVal', '')
                        field.is_item_grid = field_data.get('itemGrid', False)
                        field.include_total = field_data.get('includeTotal', False)
                        field.is_required = field_data.get('required', False)
                        field.display_in_print = field_data.get('displayInPrint', True)
                        field.subtypes = subtypes_json
                        field.is_active = field_data.get('active', True)
                        field.save()
                    except CustomField.DoesNotExist:
                        pass
                else:
                    field = CustomField.objects.create(
                        name=field_data.get('name'),
                        module_id=field_data.get('moduleId'),
                        field_type=field_data.get('fieldType'),
                        default_value=field_data.get('defaultVal', ''),
                        is_item_grid=field_data.get('itemGrid', False),
                        include_total=field_data.get('includeTotal', False),
                        is_required=field_data.get('required', False),
                        display_in_print=field_data.get('displayInPrint', True),
                        subtypes=subtypes_json,
                        is_active=field_data.get('active', True),
                        cid=cid
                    )
                return JsonResponse({'status': 'success', 'message': 'Custom field saved successfully', 'id': getattr(field, 'id', None) if 'field' in locals() else None})
                
            elif action == 'delete':
                field_id = data.get('fieldId')
                if field_id:
                    CustomField.objects.filter(id=field_id, cid=cid).delete()
                    return JsonResponse({'status': 'success', 'message': 'Custom field deleted successfully'})
                return JsonResponse({'status': 'error', 'message': 'Missing field ID'})
                
            return JsonResponse({'status': 'error', 'message': 'Invalid action'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


@method_decorator(csrf_exempt, name='dispatch')
class GeneralSettingsView(TemplateView):
    template_name = 'general_settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import GeneralSettings
        
        cid = self.request.session.get('cid', '1')
        settings, _ = GeneralSettings.objects.get_or_create(cid=cid)
        
        context['sales_form_config'] = settings.sales_form_config or '{}'
        context['sales_charges_config'] = settings.sales_charges_config or '[]'
        context['purchase_charges_config'] = settings.purchase_charges_config or '[]'
        context['receipt_charges_config'] = settings.receipt_charges_config or '[]'
        
        return context

    def post(self, request, *args, **kwargs):
        try:
            from .models import GeneralSettings
            
            data = json.loads(request.body)
            cid = request.session.get('cid', '1')
            
            settings, _ = GeneralSettings.objects.get_or_create(cid=cid)
            
            if 'sales_form_config' in data:
                settings.sales_form_config = json.dumps(data['sales_form_config'])
            if 'sales_charges_config' in data:
                settings.sales_charges_config = json.dumps(data['sales_charges_config'])
            if 'purchase_charges_config' in data:
                settings.purchase_charges_config = json.dumps(data['purchase_charges_config'])
            if 'receipt_charges_config' in data:
                settings.receipt_charges_config = json.dumps(data['receipt_charges_config'])
                
            settings.save()
            return JsonResponse({'status': 'success', 'message': 'Settings saved successfully'})
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class UsersSettingsView(TemplateView):
    template_name = 'users_settings.html'

    def get_context_data(self, **kwargs):
        from .models import AppUser, UserRole, UserActivityLog, AccessDevice, Branch, Warehouse
        context = super().get_context_data(**kwargs)
        
        users = list(AppUser.objects.values('id', 'name', 'email', 'role_id', 'role__role_name', 'phone', 'is_active', 'locations'))
        roles = list(UserRole.objects.values('id', 'role_name', 'permission_level'))
        logs = list(UserActivityLog.objects.order_by('-created_at').values('created_at', 'user_name_snapshot', 'action', 'log_type', 'transaction_type', 'extra_info'))
        devices = list(AccessDevice.objects.order_by('-last_access').values('user__name', 'os', 'browser', 'ip_address', 'status', 'last_access'))
        
        # Formatting dates to strings
        for log in logs:
            log['date'] = log['created_at'].strftime('%d/%m/%Y %I:%M %p')
            log['user'] = log['user_name_snapshot']
            log['tx'] = log['transaction_type']
            log['type'] = log['log_type']
            log['extra'] = log['extra_info']
            
        # Grouping devices by user
        device_sessions = {}
        login_activities = []
        for d in devices:
            uname = d['user__name']
            if uname not in device_sessions:
                device_sessions[uname] = []
            device_sessions[uname].append({
                'os': d['os'], 'browser': d['browser'], 'ip': d['ip_address'],
                'date': d['last_access'].strftime('%b %d, %I:%M:%S %p'),
                'status': d['status']
            })
            login_activities.append({
                'user': uname, 'os': d['os'], 'browser': d['browser'],
                'date': d['last_access'].strftime('%b %d, %I:%M:%S %p'),
                'status': d['status'], 'count': 1
            })

        formatted_users = []
        for u in users:
            formatted_users.append({
                'id': u['id'], 'name': u['name'], 'email': u['email'],
                'role': u['role__role_name'] or '', 'role_id': u['role_id'], 'phone': u['phone'] or '',
                'is_active': u['is_active'],
                'locations': u['locations'] or []
            })
            
        formatted_roles = []
        for r in roles:
            formatted_roles.append({'id': r['id'], 'name': r['role_name'], 'permission_level': r['permission_level']})

        context['users_data'] = json.dumps(formatted_users)
        context['roles_data'] = json.dumps(formatted_roles)
        context['activity_logs'] = json.dumps(logs)
        context['device_sessions'] = json.dumps(device_sessions)
        context['login_activities'] = json.dumps(login_activities)
        
        # Prepare Locations Data (Active Branches and Warehouses)
        branches = list(Branch.objects.filter(is_active=True).values('id', 'name'))
        warehouses = list(Warehouse.objects.filter(is_active=True).values('id', 'name'))
        locations_list = []
        for b in branches:
            locations_list.append({'id': f"B-{b['id']}", 'name': b['name'], 'type': 'Branch'})
        for w in warehouses:
            locations_list.append({'id': f"W-{w['id']}", 'name': w['name'], 'type': 'Warehouse'})
        context['locations_data'] = json.dumps(locations_list)
        
        from .models import Module
        groups = Module.objects.filter(menu_type='menu').prefetch_related('submodules')
        grouped_modules = {}
        for g in groups:
            subs = list(g.submodules.all())
            if subs:
                grouped_modules[g.module_name] = subs
        context['grouped_modules'] = grouped_modules
        
        context['permission_levels'] = [
            'Transactions Sales Entry', 
            'Transactions Sales & Purchase Entry', 
            'Sales Rep', 
            'Franchisee', 
            'Accountant', 
            'Administrator', 
            'Stock Keeper'
        ]
        
        return context

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            action = data.get('action')
            
            if action == 'save_user':
                from .models import AppUser, UserRole
                u_id = data.get('id')
                name = data.get('name', '')
                email = data.get('email', '')
                phone = data.get('phone', '')
                password = data.get('password', '')
                role_id = data.get('role_id', None)
                locations = data.get('locations', [])
                
                # Check for duplicate email
                if AppUser.objects.filter(email=email).exclude(id=u_id).exists():
                    return JsonResponse({'status': 'error', 'message': 'Email address is already in use.'})
                
                role_obj = None
                if role_id:
                    role_obj = UserRole.objects.filter(id=role_id).first()
                
                if u_id:
                    user = AppUser.objects.get(id=u_id)
                    user.name = name
                    user.email = email
                    user.phone = phone
                    user.role = role_obj
                    user.locations = locations
                    if password:
                        user.password = password
                    user.save()
                    msg = 'User updated successfully'
                else:
                    AppUser.objects.create(name=name, email=email, phone=phone, password=password, role=role_obj, locations=locations)
                    msg = 'User created successfully'
                return JsonResponse({'status': 'success', 'message': msg})

            elif action == 'delete_user':
                from .models import AppUser
                u_id = data.get('id')
                try:
                    AppUser.objects.filter(id=u_id).delete()
                    return JsonResponse({'status': 'success', 'message': 'User deleted successfully'})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': f'Cannot delete user: {str(e)}'})

            elif action == 'save_role':
                from .models import UserRole, UserRolePermission
                r_id = data.get('id')
                name = data.get('name', '')
                perm_level = data.get('perm_level', '')
                custom_perms = data.get('custom_permissions', {})
                
                if r_id:
                    role = UserRole.objects.get(id=r_id)
                    role.role_name = name
                    role.permission_level = perm_level
                    role.save()
                    msg = 'Role updated successfully'
                else:
                    role = UserRole.objects.create(role_name=name, permission_level=perm_level)
                    msg = 'Role created successfully'
                    
                # Save custom permissions
                UserRolePermission.objects.filter(role=role).delete()
                if custom_perms:
                    for mod_name, perms in custom_perms.items():
                        UserRolePermission.objects.create(
                            role=role,
                            module_name=mod_name,
                            can_view=perms.get('view', False),
                            can_add=perms.get('add', False),
                            can_edit=perms.get('edit', False),
                            can_delete=perms.get('delete', False),
                            extras=perms.get('extras', {})
                        )
                
                return JsonResponse({'status': 'success', 'message': msg})

            elif action == 'delete_role':
                from .models import UserRole
                r_id = data.get('id')
                UserRole.objects.filter(id=r_id).delete()
                return JsonResponse({'status': 'success', 'message': 'Role deleted successfully'})

            elif action == 'get_role_template':
                from .models import Module, UserRolePermission
                level = data.get('level', '')
                role_id = data.get('role_id', None)
                
                modules = Module.objects.all()
                template_data = {}
                for m in modules:
                    # Get the template dictionary specifically for this role level
                    perms = m.template_permissions.get(level, {})
                    if perms:
                        # Copy the dict so we can safely modify it
                        template_data[m.module_name] = dict(perms)
                        template_data[m.module_name]['base_view'] = perms.get('view', False)
                        
                if role_id:
                    custom_perms = UserRolePermission.objects.filter(role_id=role_id)
                    for cp in custom_perms:
                        if cp.module_name in template_data:
                            template_data[cp.module_name]['view'] = cp.can_view
                            template_data[cp.module_name]['add'] = cp.can_add
                            template_data[cp.module_name]['edit'] = cp.can_edit
                            template_data[cp.module_name]['delete'] = cp.can_delete
                            
                            if cp.extras:
                                for k, v in cp.extras.items():
                                    template_data[cp.module_name][k] = v
                                    
                return JsonResponse({'status': 'success', 'data': template_data})

            return JsonResponse({'status': 'error', 'message': 'Invalid action'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

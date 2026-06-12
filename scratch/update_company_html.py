import re

filepath = 'templates/company_settings.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# View mode replacements
content = re.sub(
    r'<h2 id="viewCompName"[^>]*>.*?</h2>',
    '<h2 id="viewCompName" class="text-[18px] font-extrabold text-[var(--text-primary)]">{{ company.name|default:"Company Name" }}</h2>',
    content
)

content = re.sub(
    r'<p id="viewCompAddress"[^>]*>.*?</p>',
    '<p id="viewCompAddress" class="text-[13px] text-[var(--text-secondary)] mt-1 max-w-2xl leading-relaxed">{{ company.address1|default:"" }}, {{ company.address2|default:"" }}, {{ company.city|default:"" }} - {{ company.postal_code|default:"" }}, {{ company.state|default:"" }}, {{ company.country|default:"" }}</p>',
    content,
    flags=re.DOTALL
)

content = re.sub(r'<span id="viewCompPhone"[^>]*>.*?</span>', '<span id="viewCompPhone" class="font-medium text-[var(--text-primary)]">{{ company.mobileNo|default:"-" }}</span>', content)
content = re.sub(r'<span id="viewCompEmail"[^>]*>.*?</span>', '<span id="viewCompEmail" class="font-medium text-[var(--text-primary)]">{{ company.emailId|default:"-" }}</span>', content)
content = re.sub(r'<span id="viewCompTimeZone"[^>]*>.*?</span>', '<span id="viewCompTimeZone" class="font-medium text-[var(--text-primary)]">{{ company.timezone|default:"(UTC +5:30) Indian Standard Time, Sri Lanka Time" }}</span>', content)
content = re.sub(r'<span id="viewCompBusinessType"[^>]*>.*?</span>', '<span id="viewCompBusinessType" class="font-medium text-[var(--text-primary)]">{{ company.business_type|default:"Retail Shop" }}</span>', content)
content = re.sub(r'<p id="viewTaxGSTIN"[^>]*>.*?</p>', '<p id="viewTaxGSTIN" class="text-[14px] font-bold text-[var(--text-secondary)]">{{ company.taxId|default:"-" }}</p>', content)
content = re.sub(r'<p id="viewTaxPAN"[^>]*>.*?</p>', '<p id="viewTaxPAN" class="text-[14px] font-bold text-[var(--text-secondary)]">{{ company.registrationNo|default:"-" }}</p>', content)

# Edit mode replacements
content = re.sub(r'id="editCompName" value="[^"]*"', 'id="editCompName" value="{{ company.name|default:"" }}"', content)
content = re.sub(r'id="editCompAddr1" value="[^"]*"', 'id="editCompAddr1" value="{{ company.address1|default:"" }}"', content)
content = re.sub(r'id="editCompAddr2" value="[^"]*"', 'id="editCompAddr2" value="{{ company.address2|default:"" }}"', content)
content = re.sub(r'id="editCompCity" value="[^"]*"', 'id="editCompCity" value="{{ company.city|default:"" }}"', content)
content = re.sub(r'id="editCompPostal" value="[^"]*"', 'id="editCompPostal" value="{{ company.postal_code|default:"" }}"', content)
content = re.sub(r'id="editCompPhone" value="[^"]*"', 'id="editCompPhone" value="{{ company.mobileNo|default:"" }}"', content)
content = re.sub(r'id="editCompEmail" value="[^"]*"', 'id="editCompEmail" value="{{ company.emailId|default:"" }}"', content)
content = re.sub(r'id="editTaxGSTIN" value="[^"]*"', 'id="editTaxGSTIN" value="{{ company.taxId|default:"" }}"', content)
content = re.sub(r'id="editTaxPAN" value="[^"]*"', 'id="editTaxPAN" value="{{ company.registrationNo|default:"" }}"', content)

# For textarea
content = re.sub(
    r'<textarea id="editCompAddInfo"[^>]*>.*?</textarea>',
    '<textarea id="editCompAddInfo" rows="2" class="w-full p-3 border border-[var(--border)] rounded-lg bg-[var(--surface)] text-[13px] focus:border-accent outline-none resize-none">{{ company.notes|default:"" }}</textarea>',
    content,
    flags=re.DOTALL
)

# Replace Javascript saveProfile function
js_saveProfile = """function saveProfile() {
        const name = document.getElementById('editCompName').value.trim();
        if (!name) {
            showToast('Please specify a company name.', 'error');
            return;
        }

        const data = {
            name: name,
            address1: document.getElementById('editCompAddr1').value.trim(),
            address2: document.getElementById('editCompAddr2').value.trim(),
            city: document.getElementById('editCompCity').value.trim(),
            postal_code: document.getElementById('editCompPostal').value.trim(),
            country: document.getElementById('editCompCountry').value,
            state: document.getElementById('editCompState').value,
            phone: document.getElementById('editCompPhone').value.trim(),
            email: document.getElementById('editCompEmail').value.trim(),
            timezone: document.getElementById('editCompTimeZone').value,
            business_type: document.getElementById('editCompBusType').value,
            notes: document.getElementById('editCompAddInfo').value.trim()
        };

        showToast('Saving profile details...', 'loading');
        
        fetch('{% url "company-settings" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if(result.status === 'success') {
                document.getElementById('viewCompName').innerText = data.name;
                document.getElementById('viewCompAddress').innerText = `${data.address1}, ${data.address2}, ${data.city} - ${data.postal_code}, ${data.state}, ${data.country}`;
                document.getElementById('viewCompPhone').innerText = data.phone || '-';
                document.getElementById('viewCompEmail').innerText = data.email || '-';
                document.getElementById('viewCompTimeZone').innerText = data.timezone;
                document.getElementById('viewCompBusinessType').innerText = data.business_type;

                toggleProfileEdit(false);
                showToast('Company profile updated!', 'success');
                hideToast(1500);
            } else {
                showToast(result.message || 'Error saving profile.', 'error');
            }
        })
        .catch(error => {
            showToast('Network error while saving.', 'error');
            console.error(error);
        });
    }"""

content = re.sub(r'function saveProfile\(\)\s*\{.*?(?=\n    // 2\. Taxation section helpers)', js_saveProfile + "\n", content, flags=re.DOTALL)

# Replace Javascript saveTaxation function
js_saveTaxation = """function saveTaxation() {
        const data = {
            taxId: document.getElementById('editTaxGSTIN').value.trim(),
            pan: document.getElementById('editTaxPAN').value.trim()
        };

        showToast('Saving taxation settings...', 'loading');
        
        fetch('{% url "company-settings" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if(result.status === 'success') {
                document.getElementById('viewTaxGSTIN').innerText = data.taxId || '-';
                document.getElementById('viewTaxPAN').innerText = data.pan || '-';
                document.getElementById('viewTaxMSME').checked = document.getElementById('editTaxMSME').checked;
                document.getElementById('viewTaxRate').innerText = document.getElementById('editTaxRate').value;
                document.getElementById('viewTaxBranch').innerText = document.getElementById('editTaxBranch').value.trim() || 'Main Branch';

                toggleTaxationEdit(false);
                showToast('Taxation settings updated!', 'success');
                hideToast(1500);
            } else {
                showToast(result.message || 'Error saving taxation settings.', 'error');
            }
        })
        .catch(error => {
            showToast('Network error while saving.', 'error');
            console.error(error);
        });
    }"""

content = re.sub(r'function saveTaxation\(\)\s*\{.*?(?=\n    // 3\. Logo preview logic)', js_saveTaxation + "\n", content, flags=re.DOTALL)


# Set selected options
content = content.replace(
    '<option value="India" selected>India</option>',
    '<option value="India" {% if company.country == "India" %}selected{% endif %}>India</option>'
)
content = content.replace(
    '<option value="Sri Lanka">Sri Lanka</option>',
    '<option value="Sri Lanka" {% if company.country == "Sri Lanka" %}selected{% endif %}>Sri Lanka</option>'
)
content = content.replace(
    '<option value="Tamil Nadu" selected>Tamil Nadu</option>',
    '<option value="Tamil Nadu" {% if company.state == "Tamil Nadu" %}selected{% endif %}>Tamil Nadu</option>'
)
content = content.replace(
    '<option value="Karnataka">Karnataka</option>',
    '<option value="Karnataka" {% if company.state == "Karnataka" %}selected{% endif %}>Karnataka</option>'
)
content = content.replace(
    '<option value="Kerala">Kerala</option>',
    '<option value="Kerala" {% if company.state == "Kerala" %}selected{% endif %}>Kerala</option>'
)

content = content.replace(
    '<option value="Retail Shop" selected>Retail Shop</option>',
    '<option value="Retail Shop" {% if company.business_type == "Retail Shop" %}selected{% endif %}>Retail Shop</option>'
)
content = content.replace(
    '<option value="Wholesale">Wholesale</option>',
    '<option value="Wholesale" {% if company.business_type == "Wholesale" %}selected{% endif %}>Wholesale</option>'
)
content = content.replace(
    '<option value="Manufacturing">Manufacturing</option>',
    '<option value="Manufacturing" {% if company.business_type == "Manufacturing" %}selected{% endif %}>Manufacturing</option>'
)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated template HTML.")

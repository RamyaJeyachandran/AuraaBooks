# Warehouse Management Analysis - OutputBooks

This document provides a comprehensive analysis of the **Warehouse** page and the **New Warehouse Modal** for the Output Books project, based on the frontend UI (`abproject`) and the backend logic (`outputbooks`).

## 1. Purpose
The Warehouse Management page provides a centralized interface for users to manage multiple storage locations (Warehouses). It is essential for inventory tracking, allowing businesses to segregate stock across different physical or geographical spaces. It bridges the gap between accounting ledgers and physical inventory by tying storage locations to respective branches and contact details.

## 2. Page Operations
The main Warehouse page provides several high-level operations for warehouse management:
- **Metrics Dashboard**: Quick visibility into total warehouses and their statuses (Active vs. In-Active) via count pills.
- **Listing & Data Grid**: Displays a tabular view of warehouses featuring columns for: *Stock Location Name, Contact Person, Mobile, Balance, and Action*.
- **Filtering**: 
  - Status filters (All, Active, Inactive).
  - A dropdown filter to directly search and jump to a specific warehouse.
- **Export & Import**: Extensive data interoperability options.
  - **Export to**: CSV, XLS, PDF, and Tally XML.
  - **Import from**: CSV, XLS, Tally, and Tally XML.
- **Column Settings**: A dynamic toggle to show/hide specific columns (Contact Person, GSTIN, Balance) and display archived or inactive locations.
- **Recent Navigator**: A quick-access tool to jump back to the most recently viewed or edited warehouse (e.g., WAR-001).

## 3. New Warehouse Modal Functionalities
Clicking the "Add Warehouse" button opens a comprehensive, split-screen slide-in modal.

### Header Navigation
- **Quick Links**: A dropdown menu allows users to jump instantly to creating other entities (New Customer, Supplier, Sales Rep, Branch, Franchisee, Project).
- **Save Actions**: Options to either "Save" and close, or "Save & New" to continuously add records.

### Left Section (General Details)
Collects the primary identity and contact details for the warehouse:
- **Basic Info**: Stock Location Name, Contact Person.
- **Accounting**: Ledger Name (Mandatory).
- **Taxation Details**: 
  - **GSTIN**: Includes a helper tooltip explaining the 15-digit code, along with a hidden toggle for "Registered in MSME/Udyam".
  - **PAN**: Includes a 10-digit PAN helper tooltip.
- **Communication**: Email ID, Contact Mobile (+91), Work Phone.
- **Status & Attachments**: A toggle for marking the warehouse as "Active" and a button to upload relevant files/documents.

### Right Section (Tabbed Data)
Collects geographical and financial data, separated into tabs.

**Tab 1: Address**
- **Location Fields**: Address Line 1 & 2, City/Town, Postal/Zip Code, Country, and State.
- **Branch Assignment**: A checkbox to assign the warehouse under a specific parent Branch (e.g., Main Branch).
- **Geotagging**: A Map toggle that opens a latitude/longitude input field for precise location tracking.

**Tab 2: Bank Details**
- **Core Bank Info**: Account Name, Account Number, Account Type, Bank Name, Bank Branch, IFSC Code.
- **International/Trade Codes**: Swift Code (with an 11-digit tooltip) and Authorised Dealer Code (with a 14-digit IEC tooltip).
- **Other**: Correspondent Bank textarea and an option to map the bank details under a specific branch.

## 4. Backend Table Structure Details
In the `outputbooks` CodeIgniter backend, Warehouses are conceptually treated as "Locations" and overlap with the Contacts and Storage architectures.

### `ob_contacts`
Warehouses are registered in the main contacts table under a specific `csType` (Contact/Storage Type).
- **`csType = 'L'`**: Identifies the record as a Location/Warehouse.
- **Key Columns**: `id`, `name` (Location Name), `cId` (Company ID), `bId` (Branch ID - linking it to the parent branch), `isActive`, `taxNo` (GSTIN), etc.

### `ob_contacts_address`
Stores the address configuration inputted from the "Address" tab.
- **Key Columns**: `conId` (Foreign key to `ob_contacts.id`), `addrType`, `address1`, `address2`, `city`, `state`, `country`, `zip`.

### `ob_storage`
Represents the exact storage location entity used for inventory transactions.
- **Key Columns**: `id`, `stocode` (Stock Code), `stoname` (Stock Location Name), `cId` (Company ID).

### `ob_storage_ts` / `ob_storage_cur`
These tables manage the actual tracking of stock levels at the warehouse.
- **`ob_storage_ts`**: Tracks historical transactions (in/out) for the warehouse.
- **`ob_storage_cur`**: Maintains the current available stock levels (`stkLevel`, `bags`, etc.) mapped to the `stoId` (Storage/Warehouse ID).

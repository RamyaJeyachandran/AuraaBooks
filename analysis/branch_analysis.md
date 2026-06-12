# Branch Management Analysis - OutputBooks

This document provides a comprehensive analysis of the **Branch** page and the **New Branch Modal** for the Output Books project, based on the frontend UI (`abproject`) and the backend logic (`outputbooks`).

## 1. Purpose
The Branch Management page acts as the central hub for managing multiple branches of a business entity. It is crucial for maintaining separate ledgers, configuring distinct taxation numbers (like branch-specific GSTINs), managing branch-level inventory, and separating communication/shipping details across the organization's regional offices or sub-entities.

## 2. Page Operations
The main Branch page offers the following high-level operations:
- **Metrics Dashboard**: Top-level count pills providing quick visibility into the `Total`, `Active`, and `In-Active` branches.
- **Listing & Data Grid**: A data table displaying all configured branches with columns for: *Branch Name, Contact, Location, Status (Active/Inactive toggle indicators), and Action (Edit/Delete).*
- **Filtering**:
  - Filter by statuses (All, Active, Inactive).
  - A dropdown selector to search and instantly filter to a specific branch.
- **Export & Import Tools**: 
  - **Export to**: CSV, XLS, PDF, and Tally XML.
  - **Import from**: CSV, XLS, Tally direct, and Tally XML.
- **Column Settings**: A dropdown utility to dynamically show or hide data columns (Contact Person, GSTIN, Balance) and toggles for showing archived or inactive branches.
- **Recent Navigator**: Allows the user to jump back quickly to their most recently engaged branch.

## 3. New Branch Modal Functionalities
Clicking "Add Branch" slides in a comprehensive, split-screen modal form that allows users to capture extensive details about the new branch.

### Header Navigation
- **Quick Entity Creation**: A dropdown link menu to rapidly create other related items without losing context (New Customer, Supplier, Sales Rep, Referrer, Warehouse, Franchisee, Project).
- **Save Actions**: Contains standard "Save" and "Save & New" buttons for workflow continuity.

### Left Section (General & Tax Details)
This form section captures the primary identity of the branch:
- **Basic Info**: Branch Name, Contact Name.
- **Accounting**: Ledger Name (Mandatory) to tie the branch into the general ledger.
- **Taxation Details**: 
  - **GSTIN**: Form field accompanied by a tooltip and a hidden menu for the "Registered in MSME/Udyam" toggle.
  - **PAN**: Field accompanied by a 10-digit PAN helper tooltip.
- **Communication**: Contact Mobile (+91), Work Phone, Email ID.
- **Miscellaneous**: 
  - Additional Info (Textarea).
  - **Tag Management**: A feature to link access to the branch using specific "Tags", complete with an integrated Tag creation sub-modal.
  - **Logo Upload**: Allows users to upload a branch-specific logo (recommended size 120x120 pixels).
- **Status & Attachments**: "Active" toggle and a file upload button for branch-related documents.

### Right Section (Tabbed Data)
This side is dedicated to geographic and financial configurations, spread across three tabs:

**Tab 1: Address**
- Address Line 1 & 2, City/Town, Postal/Zip Code, Country, State.
- **Map Input**: Integrated toggle to insert precise Latitude and Longitude coordinates.

**Tab 2: Shipping Address**
- Starts with a "Same as Billing Address" checkbox.
- Includes unique fields for Shipping Ref Name, Shipping GSTIN, Address Lines, Phone, Email, Location info, and its own Map Input mapping.

**Tab 3: Bank Details**
- Core Bank Info: Account Name, Account Number, Account Type, Bank Name, Bank Branch, IFSC Code.
- International Codes: Swift Code and Authorised Dealer Code.
- Correspondent Bank mapping.

**Common Footer**: An "Assign under branch" dropdown feature to establish a branch hierarchy (i.e., mapping a sub-branch to the Main Branch).

## 4. Backend Table Structure Details
In the `outputbooks` CodeIgniter backend, Branches are handled by the core contact management system, utilizing the `ob_contacts` structure alongside specific identifiers.

### `ob_contacts`
All branches are stored alongside customers and suppliers within the main contacts table, identified by their `csType`.
- **`csType = 'B'`**: Uniquely identifies the record as a Branch entity.
- **Key Columns**: `id`, `name` (Branch Name), `cId` (Company ID), `ledger_name`, `email`, `mobile`, `taxNo` (GSTIN), `panNo`, `isActive`, `tags` (for tag-based access control), and `logo` (path to uploaded logo).

### `ob_contacts_address`
Stores the geographic data points inputted from both the "Address" and "Shipping Address" tabs.
- **Key Columns**: `conId` (Foreign key pointing to `ob_contacts.id`), `addrType` (e.g., distinguishing between Billing vs. Shipping), `address1`, `address2`, `city`, `state`, `country`, `zip`.

### Bank Details and Hierarchy
- **Bank Information**: Stored either in dedicated bank JSON fields inside `ob_contacts` or related linked financial tables, utilizing columns like `bank_name`, `acc_no`, `ifsc`, etc.
- **Hierarchy (`bId`)**: If a branch is assigned *under* another branch (via the Common Assign dropdown), its `ob_contacts` record will have its `bId` (Branch ID) column pointing to the parent branch's ID.

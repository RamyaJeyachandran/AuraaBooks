CREATE TABLE IF NOT EXISTS public.tbl_company (
    id SERIAL PRIMARY KEY,
    logo text,
    name character varying(255),
    "shortName" character varying(50),
    address1 text,
    address2 text,
    "countryId" integer,
    "stateId" integer,
    "cityId" integer,
    "emailId" character varying(255),
    "mobileNo" character varying(20),
    "whatsappNo" character varying(20),
    currency character varying(10),
    "fyStart" date,
    "appDateFormat" character varying(50),
    "appColorCode" character varying(20),
    "branchLimit" integer,
    "userLimit" integer,
    isseparatedb boolean,
    dbname character varying(100),
    "isActive" boolean DEFAULT true,
    "createdBy" integer,
    "createdDt" timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    "updatedDt" timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    "updatedBy" integer,
    code character varying(50) UNIQUE
);

INSERT INTO public.tbl_company (id, code, name, address1, "mobileNo", "emailId") 
VALUES (1, 'CMP-00001', 'Test Company', '123 Test St', '1234567890', 'test@example.com')
ON CONFLICT (id) DO NOTHING;

CREATE TABLE IF NOT EXISTS public.tbl_company_details (
    id SERIAL PRIMARY KEY,
    "companyId" integer REFERENCES public.tbl_company(id) ON DELETE CASCADE,
    "registrationNo" character varying(100),
    "taxId" character varying(100),
    website character varying(255),
    notes text,
    city character varying(100),
    state character varying(100),
    country character varying(100),
    postal_code character varying(20),
    business_type character varying(100),
    timezone character varying(255),
    "createdDt" timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    "updatedDt" timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

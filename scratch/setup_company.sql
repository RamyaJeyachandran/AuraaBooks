ALTER TABLE public.tbl_company ADD COLUMN IF NOT EXISTS code character varying(50) UNIQUE;
UPDATE public.tbl_company SET code = 'CMP-00001' WHERE id = 1 AND code IS NULL;

CREATE TABLE IF NOT EXISTS public.tbl_company_details (
    id SERIAL PRIMARY KEY,
    "companyId" integer REFERENCES public.tbl_company(id) ON DELETE CASCADE,
    "registrationNo" character varying(100),
    "taxId" character varying(100),
    website character varying(255),
    notes text,
    "createdDt" timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    "updatedDt" timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

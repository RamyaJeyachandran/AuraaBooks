ALTER TABLE public.tbl_company_details ADD COLUMN IF NOT EXISTS city character varying(100);
ALTER TABLE public.tbl_company_details ADD COLUMN IF NOT EXISTS state character varying(100);
ALTER TABLE public.tbl_company_details ADD COLUMN IF NOT EXISTS country character varying(100);
ALTER TABLE public.tbl_company_details ADD COLUMN IF NOT EXISTS postal_code character varying(20);
ALTER TABLE public.tbl_company_details ADD COLUMN IF NOT EXISTS business_type character varying(100);
ALTER TABLE public.tbl_company_details ADD COLUMN IF NOT EXISTS timezone character varying(255);

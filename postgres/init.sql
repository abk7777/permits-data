GRANT ALL PRIVILEGES ON DATABASE permits TO postgres;
CREATE TABLE permits_raw (
    "Assessor Book" TEXT,
    "Assessor Page" TEXT,
    "Assessor Parcel" TEXT,
    "Tract" TEXT,
    "Block" TEXT,
    "Lot" TEXT,
    "Reference # (Old Permit #)" TEXT,
    "PCIS Permit #" TEXT,
    "Status" TEXT,
    "Status Date" TEXT,
    "Permit Type" TEXT,
    "Permit Sub-Type" TEXT,
    "Permit Category" TEXT,
    "Project Number" TEXT,
    "Event Code" TEXT,
    "Initiating Office" TEXT,
    "Issue Date" TEXT,
    "Address Start" TEXT,
    "Address Fraction Start" TEXT,
    "Address End" TEXT,
    "Address Fraction End" TEXT,
    "Street Direction" TEXT,
    "Street Name" TEXT,
    "Street Suffix" TEXT,
    "Suffix Direction" TEXT,
    "Unit Range Start" TEXT,
    "Unit Range End" TEXT,
    "Zip Code" TEXT,
    "Work Description" TEXT,
    "Valuation" TEXT,
    "Floor Area-L.A. Zoning Code Definition" TEXT,
    "# of Residential Dwelling Units" TEXT,
    "# of Accessory Dwelling Units" TEXT,
    "# of Stories" TEXT,
    "Contractor's Business Name" TEXT,
    "Contractor Address" TEXT,
    "Contractor City" TEXT,
    "Contractor State" TEXT,
    "License Type" TEXT,
    "License #" TEXT,
    "Principal First Name" TEXT,
    "Principal Middle Name" TEXT,
    "Principal Last Name" TEXT,
    "License Expiration Date" TEXT,
    "Applicant First Name" TEXT,
    "Applicant Last Name" TEXT,
    "Applicant Business Name" TEXT,
    "Applicant Address 1" TEXT,
    "Applicant Address 2" TEXT,
    "Applicant Address 3" TEXT,
    "Zone" TEXT,
    "Occupancy" TEXT,
    "Floor Area-L.A. Building Code Definition" TEXT,
    "Census Tract" TEXT,
    "Council District" TEXT,
    "Latitude/Longitude" TEXT,
    "Applicant Relationship" TEXT,
    "Existing Code" TEXT,
    "Proposed Code" TEXT
);
SET statement_timeout = '2s';
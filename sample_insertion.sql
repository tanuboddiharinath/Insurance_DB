select * from region;

select * from insurance_types;

select COUNT(*) from branch_details
where BRANCH_NAME LIKE '%HDFC%';

select * from companies;
ALTER TABLE COM_BRANCH 
DROP column BRANCH_ID;
SELECT * FROM COM_BRANCH;

DESC COM_BRANCH;

ALTER TABLE COM_BRANCH
ADD constraint PRIMARY KEY(BRANCH_NAME);





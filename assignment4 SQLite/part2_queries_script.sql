/*1: count records in table*/
select count(*) from emp;

/*2: group data in table, print highest value for each category*/
/*print highest average weekly wage per county in 1985*/
select emp_county, emp_industry, emp_avg_weekly
from emp
where emp_year=1995
and emp_countyID !=999
and emp_countyID !=0
order by emp_avg_weekly desc;

/*3: display 3 important fields, alphabetically, only show first 10 records*/
/*fields=county, averge employment, industry*/
select emp_county, emp_avg_employ, emp_industry
from emp
where emp_year=1980	
and emp_avg_employ>=80000	
and emp_countyID>0
and emp_industryID>0
order by emp_industry
limit 10;

/*4: use GROUP BY to find averages on a numerical field */
/*average wage in new york county in 2000*/
select emp_county, avg(emp_avg_annual)
from emp
where emp_year=2000
and emp_countyID !=0
group by emp_county;


/*5: user friendly listing of the first 15 records in alpha order*/
select  emp_year || " weekly wage = "|| emp_avg_weekly||" = " ||emp_total_wage ||" / " ||emp_avg_employ || " / 52"
as " statewide average weekly wage = total wages / average employment / 52"
from emp
limit 15;


/*6: what are the counties with the higest employment*/
select emp_county, emp_avg_employ
from emp
where emp_year = 1995
and emp_industryID =0
and emp_countyID !=0
group by emp_county
order by emp_avg_employ desc
limit 20;


/*7: what are the counties with the lowest annual wages*/
select emp_county, emp_total_wage
from emp
where emp_year = 1995
and emp_industryID =0
group by emp_county
order by emp_total_wage
limit 20;


/*8: annual wages for each industry in new york city*/
select emp_industry, emp_avg_annual
from emp
where emp_year = 1995
and emp_countyID = 61
and emp_industryID != 0
group by emp_industry
order by emp_avg_annual;

/*9: statewide, what percentage is each industry of total employment*/
select emp_industry, (emp_avg_employ*100.00/5837283) as "% of total employment"
from emp
where emp_year=1975
and emp_industryID != 0
and emp_countyID = 0;


/*10: per county, what percentage is each county of total state employment*/
select emp_county, (emp_avg_employ*100.00/5837283) as "% of total state employment"
from emp
where emp_year=1975
and emp_industryID = 0
and emp_countyID !=0;




# FULL FINAL CODE

# Import modules
import pandas as pd

# Load data files
school_data_load = "Resources/schools_complete.csv"
student_data_load = "Resources/students_complete.csv"

# Read data files and store into Pandas DataFrames
school_data_df = pd.read_csv(school_data_load)
student_data_df = pd.read_csv(student_data_load)

# Combine the data into a single dataset  
school_data_all_df = pd.merge(student_data_df, school_data_df, how="left", on=["school_name", "school_name"])
school_data_all_df

# get column names for easy reference
school_data_all_df.columns

# DISTRICT SUMMARY

# calculate total number of schools
tot_schools = len(pd.unique(school_data_df['school_name']))
tot_schools

# calculate total number of students
tot_students_dist = student_data_df['Student ID'].count()
tot_students_dist

# calculate total budget
tot_budget_dist = school_data_df['budget'].sum()
tot_budget_dist

# calculate average math score
avg_math_dist = student_data_df['math_score'].mean()
avg_math_dist

# caluclate average reading score
avg_read_dist = student_data_df['reading_score'].mean()
avg_read_dist

# calculate % passing math
pass_math_dist = len(school_data_all_df.loc[school_data_all_df['math_score'] > 69]) / tot_students_dist * 100
pass_math_dist

# calculate % passing reading
pass_read_dist = len(school_data_all_df.loc[school_data_all_df['reading_score'] > 69]) / tot_students_dist * 100
pass_read_dist

# calculate % passing both math and reading
pass_mathread_dist = len(school_data_all_df.loc[(school_data_all_df['math_score'] > 69) & (
    school_data_all_df['reading_score'] > 69)]) / tot_students_dist * 100

pass_mathread_dist

# create District Summary DataFrame
dist_summary_df = pd.DataFrame(
    {"Total # of Schools": [tot_schools],
     "Total # of Students": [tot_students_dist],
     "Total Budget": [tot_budget_dist],
     "Average Math Score": [avg_math_dist],
     "Average Reading Score": [avg_read_dist],
     "% Passing Math": [pass_math_dist],
     "% Passing Reading": [pass_read_dist],
     "% Overall Passing": [pass_mathread_dist]
     }
)

# format District Summary columns
dist_summary_df["Total # of Students"] = dist_summary_df["Total # of Students"].map("{:,}".format)
dist_summary_df["Total Budget"] = dist_summary_df["Total Budget"].map("${:,}".format)
dist_summary_df["Average Math Score"] = dist_summary_df["Average Math Score"].map("{:.0f}".format)
dist_summary_df["Average Reading Score"] = dist_summary_df["Average Reading Score"].map("{:.0f}".format)
dist_summary_df["% Passing Math"] = dist_summary_df["% Passing Math"].map("{:.1f}%".format)
dist_summary_df["% Passing Reading"] = dist_summary_df["% Passing Reading"].map("{:.1f}%".format)
dist_summary_df["% Overall Passing"] = dist_summary_df["% Overall Passing"].map("{:.1f}%".format)

print("DISTRICT SUMMARY")
dist_summary_df

# SCHOOL SUMMARY

# get school type
school_type = school_data_df.set_index(['school_name'])['type']
school_type

# calculate total student count per school
student_count = school_data_all_df['school_name'].value_counts()
student_count

# calculate total budget per school
school_budget = school_data_all_df.groupby(['school_name']).mean()['budget']
school_budget

# calculate total budget per student per school
student_budget = school_budget / student_count
student_budget

# calculate average math score
math_avg = school_data_all_df.groupby(['school_name']).mean()['math_score']
math_avg

# calculate average reading score
read_avg = school_data_all_df.groupby(['school_name']).mean()['reading_score']
read_avg

# calculate % passing math

# get count of students passing math
pass_math_sch = school_data_all_df[(school_data_all_df['math_score'] > 69)]

# group students passing math by school
pass_math_sch = pass_math_sch.groupby(['school_name']).count()['student_name']

# get % of students passing math
pass_math_sch = pass_math_sch / student_count * 100
pass_math_sch

# calculate % passing reading

# get count of students passing reading
pass_read_sch = school_data_all_df[(school_data_all_df['reading_score'] > 69)]

# group students passing math by school
pass_read_sch = pass_read_sch.groupby(['school_name']).count()['student_name']

# get % of students passing math
pass_read_sch = pass_read_sch / student_count * 100
pass_read_sch

# calculate % passing math and reading (both)

# get count of students passing both
pass_both = school_data_all_df[(school_data_all_df['math_score'] > 69) & (school_data_all_df['reading_score'] > 69)]

# group students passing both by school
pass_both = pass_both.groupby(['school_name']).count()['student_name']

# get % of students passing both
pass_both = pass_both / student_count * 100
pass_both

# create School Summary DataFrame
school_summary_df = pd.DataFrame({
    "School Type": school_type,
    "Total Students": student_count,
    "Total School Budget": school_budget,
    "Per Student Budget": student_budget,
    "Average Math Score": math_avg,
    "Average Reading Score": read_avg,
    "% Passing Math": pass_math_sch,
    "% Passing Reading": pass_read_sch,
    "% Overall Passing": pass_both
    }
)

# format School Summary columns
school_summary_df["Total Students"] = school_summary_df["Total Students"].map("{:,}".format)
school_summary_df["Total School Budget"] = school_summary_df["Total School Budget"].map("${:,.2f}".format)
school_summary_df["Per Student Budget"] = school_summary_df["Per Student Budget"].map("${:.2f}".format)
school_summary_df["Average Math Score"] = school_summary_df["Average Math Score"].map("{:.0f}".format)
school_summary_df["Average Reading Score"] = school_summary_df["Average Reading Score"].map("{:.0f}".format)
school_summary_df["% Passing Math"] = school_summary_df["% Passing Math"].map("{:.1f}%".format)
school_summary_df["% Passing Reading"] = school_summary_df["% Passing Reading"].map("{:.1f}%".format)
school_summary_df["% Overall Passing"] = school_summary_df["% Overall Passing"].map("{:.1f}%".format)

print("SCHOOL SUMMARY")
school_summary_df

# SORT AND DISPLAY Top 5 Performing Schools (By % Overall Passing)

school_summary_df.sort_values(by=['% Overall Passing'], ascending=False, inplace=True)

print('TOP PERFORMING SCHOOLS BY % OVERALL PASSING')
school_summary_df.head(5)

# SORT AND DISPLAY Bottom 5 Performing Schools (By % Overall Passing)

school_summary_df.sort_values(by=['% Overall Passing'], ascending=True, inplace=True)

print('BOTTOM PERFORMING SCHOOLS BY % OVERALL PASSING')
school_summary_df.head(5)

# MATH SCORES BY GRADE

# get list of grade level values for reference
school_data_all_df.grade.unique()

# create series for each grade using conditional statements
ninth_grade = school_data_all_df[(school_data_all_df['grade'] == '9th')]
tenth_grade = school_data_all_df[(school_data_all_df['grade'] == '10th')]
eleventh_grade = school_data_all_df[(school_data_all_df['grade'] == '11th')]
twelfth_grade = school_data_all_df[(school_data_all_df['grade'] == '12th')]

# group each grade series by school and get avg math score
ninth_grade_math = ninth_grade.groupby(['school_name']).mean()['math_score']
tenth_grade_math = tenth_grade.groupby(['school_name']).mean()['math_score']
eleventh_grade_math = eleventh_grade.groupby(['school_name']).mean()['math_score']
twelfth_grade_math = twelfth_grade.groupby(['school_name']).mean()['math_score']

# create Math Scores by Grade DataFrame
math_scores_by_grade = pd.DataFrame({
    "9th": ninth_grade_math,
    "10th": tenth_grade_math,
    "11th": eleventh_grade_math,
    "12th": twelfth_grade_math
    }
)

# format Math Scores columns
math_scores_by_grade["9th"] = math_scores_by_grade["9th"].map("{:.2f}".format)
math_scores_by_grade["10th"] = math_scores_by_grade["10th"].map("{:.2f}".format)
math_scores_by_grade["11th"] = math_scores_by_grade["11th"].map("{:.2f}".format)
math_scores_by_grade["12th"] = math_scores_by_grade["12th"].map("{:.2f}".format)

# remove Index title 'school_name'
math_scores_by_grade.index.name = None

print('MATH SCORES BY GRADE')
math_scores_by_grade.head()

# READING SCORES BY GRADE

# can use MATH SCORES BY GRADE series for each grade using conditional statements

# group each grade series by school and get avg reading score
ninth_grade_read = ninth_grade.groupby(['school_name']).mean()['reading_score']
tenth_grade_read = tenth_grade.groupby(['school_name']).mean()['reading_score']
eleventh_grade_read = eleventh_grade.groupby(['school_name']).mean()['reading_score']
twelfth_grade_read = twelfth_grade.groupby(['school_name']).mean()['reading_score']

# create Reading Scores by Grade DataFrame
read_scores_by_grade = pd.DataFrame({
    "9th": ninth_grade_read,
    "10th": tenth_grade_read,
    "11th": eleventh_grade_read,
    "12th": twelfth_grade_read
    }
)

# format Reading Scores columns
read_scores_by_grade["9th"] = read_scores_by_grade["9th"].map("{:.2f}".format)
read_scores_by_grade["10th"] = read_scores_by_grade["10th"].map("{:.2f}".format)
read_scores_by_grade["11th"] = read_scores_by_grade["11th"].map("{:.2f}".format)
read_scores_by_grade["12th"] = read_scores_by_grade["12th"].map("{:.2f}".format)

# remove Index title 'school_name'
read_scores_by_grade.index.name = None

print('READING SCORES BY GRADE')
read_scores_by_grade.head()

# SCORES BY SCHOOL SPENDING

# REF DataFrame --> school_summary_df
# REF Budget/student --> student_budget = school_budget / student_count

# create spending bins and names
spending_bins = [0, 584, 629, 644, 680]
bin_names = ['<$585', '$585-630', '$630-645', '$645-680']

# add spending bins/groups to school_summary_df DataFrame
school_summary_df['Spending Ranges (Per Student)'] = pd.cut(student_budget, spending_bins, labels=bin_names)
school_summary_df

# group DataFrame by spending range and get math and read score averages, and % pass averages

# assign the dtype to variables to calculate average/mean
# --> learned this after repeated errors on run
# --> found how to remove % on stack overflow
school_summary_df['Average Math Score'] = school_summary_df['Average Math Score'].astype(int)
school_summary_df['Average Reading Score'] = school_summary_df['Average Reading Score'].astype(int)
school_summary_df['% Passing Math'] = school_summary_df['% Passing Math'].str.rstrip('%').astype(float)
school_summary_df['% Passing Reading'] = school_summary_df['% Passing Reading'].str.rstrip('%').astype(float)
school_summary_df['% Overall Passing'] = school_summary_df['% Overall Passing'].str.rstrip('%').astype(float)

# group series by Spending Range and get averages of columns
school_spend_math = school_summary_df.groupby(['Spending Ranges (Per Student)']).mean()['Average Math Score']
school_spend_read = school_summary_df.groupby(['Spending Ranges (Per Student)']).mean()['Average Reading Score']
school_spend_pass_math = school_summary_df.groupby(['Spending Ranges (Per Student)']).mean()['% Passing Math']
school_spend_pass_read = school_summary_df.groupby(['Spending Ranges (Per Student)']).mean()['% Passing Reading']
school_spend_pass_both = school_summary_df.groupby(['Spending Ranges (Per Student)']).mean()['% Overall Passing']

# create the School Spending DataFrame
school_spending_df = pd.DataFrame({
    "Average Math Score": school_spend_math,
    "Average Reading Score": school_spend_read,
    "% Passing Math": school_spend_pass_math,
    "% Passing Reading": school_spend_pass_read,
    "% Overall Passing": school_spend_pass_both
})

# format School Spending columns
school_spending_df["Average Math Score"] = school_spending_df["Average Math Score"].map("{:.2f}".format)
school_spending_df["Average Reading Score"] = school_spending_df["Average Reading Score"].map("{:.2f}".format)
school_spending_df["% Passing Math"] = school_spending_df["% Passing Math"].map("{:.2f}%".format)
school_spending_df["% Passing Reading"] = school_spending_df["% Passing Reading"].map("{:.2f}%".format)
school_spending_df["% Overall Passing"] = school_spending_df["% Overall Passing"].map("{:.2f}%".format)

print('SCORES BY SCHOOL SPENDING')
school_spending_df

# SCORES BY SCHOOL SIZE

# REF DataFrame --> school_summary_df
# REF Student count --> student_count = school_data_all_df['school_name'].value_counts() 

# create size bins and names
size_bins = [0, 999, 1999, 5000]
size_bin_names = ['Small (<1000)', 'Medium (1000-2000)', 'Large (2000-5000)']

# add size bins/groups to the school_summary_df DataFrame
school_summary_df['School Size'] = pd.cut(student_count, size_bins, labels=size_bin_names)
school_summary_df

# group DataFrame by size range and get math and read score averages, and % pass averages

# dtype for variables to calculate average/mean remains same as with SCORES BY SCHOOL SPENDING

# group series by School Size and get averages of columns
school_size_math = school_summary_df.groupby(['School Size']).mean()['Average Math Score']
school_size_read = school_summary_df.groupby(['School Size']).mean()['Average Reading Score']
school_size_pass_math = school_summary_df.groupby(['School Size']).mean()['% Passing Math']
school_size_pass_read = school_summary_df.groupby(['School Size']).mean()['% Passing Reading']
school_size_pass_both = school_summary_df.groupby(['School Size']).mean()['% Overall Passing']

# create School Size DataFrame
school_size_df = pd.DataFrame({
    "Average Math Score": school_size_math,
    "Average Reading Score": school_size_read,
    "% Passing Math": school_size_pass_math,
    "% Passing Reading": school_size_pass_read,
    "% Overall Passing": school_size_pass_both
})

# format School Size columns
school_size_df["Average Math Score"] = school_size_df["Average Math Score"].map("{:.2f}".format)
school_size_df["Average Reading Score"] = school_size_df["Average Reading Score"].map("{:.2f}".format)
school_size_df["% Passing Math"] = school_size_df["% Passing Math"].map("{:.2f}%".format)
school_size_df["% Passing Reading"] = school_size_df["% Passing Reading"].map("{:.2f}%".format)
school_size_df["% Overall Passing"] = school_size_df["% Overall Passing"].map("{:.2f}%".format)

print('SCORES BY SCHOOL SIZE')
school_size_df

# SCORES BY SCHOOL TYPE

# group series by School Type and get averages of columns
school_type_math = school_summary_df.groupby(['School Type']).mean()['Average Math Score']
school_type_read = school_summary_df.groupby(['School Type']).mean()['Average Reading Score']
school_type_pass_math = school_summary_df.groupby(['School Type']).mean()['% Passing Math']
school_type_pass_read = school_summary_df.groupby(['School Type']).mean()['% Passing Reading']
school_type_pass_both = school_summary_df.groupby(['School Type']).mean()['% Overall Passing']

# create School Type DataFrame
school_type_df = pd.DataFrame({
    "Average Math Score": school_type_math,
    "Average Reading Score": school_type_read,
    "% Passing Math": school_type_pass_math,
    "% Passing Reading": school_type_pass_read,
    "% Overall Passing": school_type_pass_both
})

# format School Type columns
school_type_df["Average Math Score"] = school_type_df["Average Math Score"].map("{:.2f}".format)
school_type_df["Average Reading Score"] = school_type_df["Average Reading Score"].map("{:.2f}".format)
school_type_df["% Passing Math"] = school_type_df["% Passing Math"].map("{:.2f}%".format)
school_type_df["% Passing Reading"] = school_type_df["% Passing Reading"].map("{:.2f}%".format)
school_type_df["% Overall Passing"] = school_type_df["% Overall Passing"].map("{:.2f}%".format)

print('SCORES BY SCHOOL TYPE')
school_type_df
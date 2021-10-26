
TYPE_GENDER = (("Male", 'Male'), ("Female", 'Female'), ("Other", 'Other'))

PRIORITY = (("Low", 'Low'), ("Medium", 'Medium'), ("High", 'High'))

STATUS = (("TODO",'To do'), ('PROCESSING', 'Processing'), ('QA', 'QA'), ('DONE', 'Done'))

FEATURE, BUG =  range(2)
LABEL = [
        (FEATURE, "Feature"),
        (BUG, 'Bug')
]
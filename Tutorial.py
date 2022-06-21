# Without this, we can't use anything from 'psphelper.py'
import psphelper;

# Introduction
print("Hello, this tutorial shows you how to use the functions in 'psphelper.py'")
input("Press ENTER to proceed.\n")

# Tutorial 1 - Clear Screen
print("Before we begin, let me tell you a story...")
input("Press ENTER to view the story.\n")

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Dolor sed viverra ipsum nunc aliquet bibendum enim. In massa tempor nec feugiat. 
Nunc aliquet bibendum enim facilisis gravida. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper. 
Amet luctus venenatis lectus magna fringilla.\n""")

print("Do you understand the story? I don't understand the story either.\n")
print("Oops! I missed the title of the story!.\n")
print("Let's rewrite the story with the title again.\n")
input("Press ENTER to clear the screen (and therefore the story as well).")
psphelper.ClearScreen()

# Tutorial 2 - .center() with fillchar
print("The title of the story is 'LOREM IPSUM'.\n")
print("Let me put the title on top of the story, aligned at the center.\n")
title = "LOREM IPSUM"
fillchar = "*"
print(title.center(50, fillchar))
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Dolor sed viverra ipsum nunc aliquet bibendum enim. 
In massa tempor nec feugiat. 
Nunc aliquet bibendum enim facilisis gravida. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper. 
Amet luctus venenatis lectus magna fringilla.\n""")

print("Not the nicest title design, but it should be easy to understand.\n")
input("Press ENTER to move on.")
psphelper.ClearScreen()

# Tutorial 3 - Show a Table
print("Let's show a table of students' coursework marks.\n")

names = ["Alice", "Bob", "Cindy"]
subjects = ["Engineering", "Arts", "Programming", "Business"]
print("We have {0} students: {1}".format(len(names), names))
print("We have {0} subjects: {1}".format(len(subjects), subjects))

# Each student's marks are in a list
marksList = [ 
    [20.5, None, 41.0, 82.39], # Alice's marks
    [None, 53.1, 91.26, 65.1], # Bob's marks
    [64.5, 33.321, None, None], # Cindy's marks
]

print("The students' marks are stored as a list of list.\n")
print("Here's the table storing students' marks.\n")
print("The title of the table is 'Coursework'.\n")
print("Students' appears as row names, while Subjects' appears as column names.\n")
title = "Coursework"
psphelper.ShowTableByList(title, names, subjects, marksList)

print("Here's what happens when row names are omitted.\n")
psphelper.ShowTableByList(title, [], subjects, marksList)
input("Press ENTER to move on.")
psphelper.ClearScreen()

print("We can store a students marks as a dictionary instead.\n")

# Each student's marks are in a dictionary
marksDictList = [ 
    {"Engineering": 20.5, "Programming": 41.0, "Business": 82.39}, # Alice's marks
    {"Arts": 53.1, "Programming": 91.26, "Business": 65.1}, # Bob's marks
    {"Engineering": 64.5, "Arts": 33.321}, # Cindy's marks
];

print("To display such data. We use ShowTableByDictionary() as follows.\n")

# Show table (data stored as list of dictionary)
psphelper.ShowTableByDictionary(title, names, subjects, subjects, marksDictList);

print("That's all for the tutorial. Good bye.\n")

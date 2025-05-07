from syllabus_pdf_generator import generate_syllabus_pdf, combine_syllabi_pdfs

syllabus = {
  "course_code": "UQ24CA651A",
  "course_title": "Programming with Python",
  "course_credits": "4-0-2-5-5",
  "program": "MCA",
  "about_course": {
    "course_objectives": "• Introduce students to the fundamentals of Python programming language and data structures.  • Provide learners with a comprehensive understanding of Object-Oriented Programming principles and advanced concepts in Python  • Mastererror handling, and file I/O operations.  • Understand the structure of a Flask application and configure Flask-SQLAlchemy for database integration in Flask applications.",
    "course_overview": "The Object-Oriented Python course equips students with a thorough understanding of Python programming, data structures, and OOP principles. The course covers a range of topics, including writing efficient Python code, designing and implementing classes and objects using OOP fundamentals, advanced OOP concepts, and web development with Python web frameworks. Students will also gain hands-on experience through experiential learning activities and a final project that demonstrates their ability to apply their skills to real-world problems.  Python is a versatile and widely used programming language, making this course highly relevant in today's technology-driven world. With a focus on creating scalable and maintainable software using OOP principles, students will develop highly sought-after skills that are applicable across multiple industries. Upon completion, students will have a solid foundation in Python and OOP, enabling them to tackle various software development challenges with confidence and provide a competitive edge in the job market."
  },
  "course_content": {
    "unit1": {
      "title": "Python Basics and Data Structures",
      "topics": [
        "Introduction to Python - History of Python",
        "Introduction to Python - Advantages of using Python",
        "Introduction to Python -  Review of Data types",
        "Functions - Defining functions",
        "Functions - Parameters and arguments",
        "Functions -  Return statement",
        "Functions - Scope of variables Random package",
        "Comprehensions - Syntax of comprehensions",
        "Comprehensions - Examples of comprehensions",
        "Iterators and Decorators - Creating iterators and decorators",
        "Iterators and Decorators - Examples of iterators and decorators"
      ],
      "experiential_learning": [
        "Worksheets on Data Types",
        "Control Structures",
        "Implement Functions",
        "comprehensions",
        "decorators"
      ],
      "no_of_hours": "14+7 Hours"
    },
    "unit2": {
      "title": "Object-Oriented Programming (OOP) and Advanced Concepts",
      "topics": [
        "Introduction to OOP - Explanation of OOP",
        "Introduction to OOP - uses",
        "Introduction to OOP - comparison with procedural programming",
        "Classes, Objects, and Inheritance - Creating and handling classes (__init__)",
        "Classes, Objects, and Inheritance - objects",
        "Classes, Objects, and Inheritance - static variables",
        "Classes, Objects, and Inheritance -  understanding inheritance and polymorphism",
        "Encapsulation, Constructors, and Destructors - Understanding encapsulation",
        "Encapsulation, Constructors, and Destructors - using constructors and destructors for object management",
        "Advanced OOP Concepts -  Delving into static and class methods",
        "Advanced OOP Concepts - class variables",
        "Composition and aggregation, Metaclasses, Introspection"
      ],
      "experiential_learning": [
        "Use hands-on examples to understand OOP concepts and compare them with procedural programming.",
        "Create classes and objects, practice using constructors and destructors.",
        "Apply inheritance and polymorphism by designing classes in a real-world model.",
        "Explore encapsulation by using private members.",
        "Finally, interact with advanced OOP concepts like static and class methods, static variables, and get to understand the power of composition and aggregation.",
        " Create classes dynamically."
      ],
      "no_of_hours": "14+7 Hours"
    },
    "unit3": {
      "title": "Exception Handling, File I/O, Modules and Packages",
      "topics": [
        "Error Handling - Introduction to errors and exceptions in Python",
        "Error Handling - handling exceptions",
        "Error Handling - raising exceptions",
        "Error Handling - creating custom exceptions",
        "File I/O Operations - Understanding reading and writing CSV, JSON, and XML files",
        "File I/O Operations - object serialization with Pickle",
        "Python Modules and Packages -  Exploring modules",
        "Python Modules and Packages -  import statements",
        "Python Modules and Packages - packages, and directory structure",
        "Python Standard Library - Overview of Python Standard Library",
        "Python Standard Library - usage of datetime, os, sys and collections modules"
      ],
      "experiential_learning": [
        "Experience error handling firsthand by raising, catching, and handling exceptions in real scenarios.",
        "Learn to perform file operations with CSV, JSON, and XML files, and grasp object serialization with Pickle. Work with Python's modules and packages, exploring their structure and import mechanics.”,“Understand Python's standard library modules like datetime, os, sys and collections through practical usage."
      ],
      "no_of_hours": "14+7 Hours"
    },
    "unit4": {
      "title": "Web Frameworks",
      "topics": [
        "Introduction to Flask",
        "Flask Basics",
        "Flask application structure - Routes and view functions",
        "Templates with Jinja2",
        "Static files",
        "Flask Forms and User Input - Flask-WTF",
        "Creating and rendering forms",
        "Form validation",
        "Handling user input",
        "Building a Simple Flask Application",
        "Flask-SQLAlchemy and Databases - Configuring Flask-SQLAlchemy",
        "Flask-SQLAlchemy and Databases - Creating models",
        "Flask-SQLAlchemy and Databases - Basic CRUD operations",
        "Deploying the Application on Cloud"
      ],
      "experiential_learning": [
        "Designing the application - Setting up models - views, and templates - Adding user input and form handling - Implementing basic functionality",
        "Get exposed to knowledge of Flask-SQLAlchemy by setting up databases, creating models, and performing CRUD operations.",
        "Design, build, and implement a simple Flask application. Deploy their application (Flask) on PythonAnywhere."
      ],
      "no_of_hours": "14+7 Hours"
    }
  },
  "textbooks": "1. Python 3 Object Oriented Programming, Dusty Philips, Packt, 3rd Edition, 2018  2. Programming Python: Powerful Object-Oriented Programming, Mark Lutz, O'Reilly Media, Fourth Edition, 2021",
  "reference_books": "1. Flask Web Development: Developing Web Applications with Python, Miguel Grinberg, O'Reilly, 2nd edition, 2018  2. Python 3: The Comprehensive Guide to Hands-On Python Programming, Johannes Ernesti, Peter Kaiser, Rheinwerk Computing, 2022  3. Python Crash Course: A Hands-On, Project-Based Introduction to Programming, E. Matthes, No Starch Press, US; 3rd edition (12 January 2023)"
}



pdf_bytes = generate_syllabus_pdf(syllabus)

# Save for testing (Optional)
with open("single_syllabus.pdf", "wb") as f:
    f.write(pdf_bytes)

# syllabi = [
#     {
#     "year": "2022",
#     "program": "MCA",
#     "course_code": "UQ22CA751A",
#     "syllabus": {
#         "unit_1": {
#         "title": "Java Fundamentals",
#         "topics": [
#             "Object-Oriented Programming",
#             "JDK",
#             "Data types",
#             "Operators",
#             "Program control statements - if",
#             "Program control statements - switch",
#             "Program control statements - for",
#             "Program control statements - while",
#             "Classes",
#             "Objects and Methods",
#             "Myths and Facts about Java classes and objects",
#             "Constructors",
#             "Static and Heap memory",
#             "new keyword",
#             "Garbage Collection and finalizers",
#             "this keyword",
#             "Arrays and jagged arrays",
#             "Array References",
#             "length Member",
#             "for loops",
#             "for-each",
#             "Strings",
#             "Command-Line Arguments",
#             "Method Overloading",
#             "Overloading Constructors",
#             "Nested Classes."
#         ],
#         "experiential_learning": [
#             "Problem solving with data types",
#             "Loops",
#             "Arrays",
#             "Garbage Collection",
#             "Polymorphism."
#         ]
#         },
#         "unit_2": {
#         "title": "Inheritance and Multithreading",
#         "topics": [
#             "Inheritance",
#             "Member Access",
#             "Constructors",
#             "Method Overriding",
#             "Abstract Classes",
#             "Exception Handling",
#             "Interfaces and Packages",
#             "Multithreaded Programming",
#             "Thread Communication Using notify()",
#             "wait() and notifyAll()",
#             "String Handling",
#             "Enumeration and Annotations",
#             "Wrappers Class."
#         ],
#         "experiential_learning": [
#             "Problem solving with Inheritance",
#             "Exception handling",
#             "Multi-threading",
#             "Annotations."
#         ]
#         },
#         "unit_3": {
#         "title": "JDBC and Servlets",
#         "topics": [
#             "JDBC classes and interfaces",
#             "Talking to Database",
#             "Immediate Solution",
#             "Essential JDBC program",
#             "Using Prepared Statement Object",
#             "Interactive SQL Tool",
#             "types of JDBC",
#             "JDBC in Action - Result Sets",
#             "JDBC in Action - Batch updates",
#             "JDBC in Action - Mapping",
#             "JDBC in Action - Basic JDBC data types",
#             "JDBC in Action - Advanced JDBC datatypes",
#             "JDBC in Action - Immediate Solutions",
#             "Web Application Server",
#             "Server Architecture",
#             "Servlet Structure",
#             "Servlet Creation",
#             "Servlet's Lifecycle",
#             "Single Thread model interface",
#             "Handling Client Request: Form Data",
#             "Handling Client Request: HTTP Request Headers",
#             "Generating Server Response: HTTP Response Headers",
#             "Inter-Servlet communication",
#             "Handling Cookies",
#             "Session Tracking."
#         ],
#         "experiential_learning": [
#             "Problem solving JDBC",
#             "Problem solving using Servlets",
#             "Cookies and Sessions."
#         ]
#         },
#         "unit_4": {
#         "title": "JSP, Annotations, Frameworks",
#         "topics": [
#             "Overview of JSP Technology",
#             "Need of JSP",
#             "Benefits of JSP",
#             "Advantages of JSP",
#             "Basic Syntax",
#             "Invoking Java Code with JSP Scripting Elements",
#             "Using JSP expressions",
#             "Using Scriplets",
#             "Declarations",
#             "Creating Packages",
#             "JAR files",
#             "Annotations",
#             "Annotation types",
#             "working with Java Bean",
#             "Frameworks - Hibernate",
#             "Frameworks - Struts",
#             "Frameworks - Spring"
#         ],
#         "experiential_learning": [
#             "Working with JSP scripting elements",
#             "annotations and creating JAR files."
#         ]
#         }
#     }
#     },
#     {
#     "year": "2023",
#     "program": "MCA",
#     "course_code": "UQ23CA751A",
#     "syllabus": {
#         "unit_1": {
#         "title": "Java Fundamentals and OOP",
#         "topics": [
#             "Overview of Java",
#             "Basic Java Concepts",
#             "JDK",
#             "JVM",
#             "JRE",
#             "Building Blocks of Java - Keywords",
#             "Building Blocks of Java - Methods",
#             "Building Blocks of Java - Control Flow",
#             "Building Blocks of Java - Loops",
#             "Building Blocks of Java - Operators",
#             "Arrays",
#             "Strings",
#             "Introduction to OOP",
#             "Classes and Objects",
#             "Constructor",
#             "Interfaces and Abstract Classes",
#             "Inheritance in Java",
#             "Polymorphism - Method Overloading",
#             "Polymorphism - Method Overriding",
#             "Polymorphism - Dynamic Method Dispatch",
#             "Wrapper Classes and Autoboxing"
#         ],
#         "experiential_learning": [
#             "Programs on decision making and loops",
#             "Programs on Inheritance",
#             "Polymorphism",
#             "Programs implementing autoboxing",
#             "Array and String Handling"
#         ]
#         },
#         "unit_2": {
#         "title": "Advanced Java Concepts",
#         "topics": [
#             "Encapsulation and Access Specifiers",
#             "Exception Handling",
#             "Threads - Multithreading",
#             "Threads - Thread Communication",
#             "Collections Framework in Java - Introduction to Collections",
#             "Collections Framework in Java - Map",
#             "Collections Framework in Java - Set",
#             "Collections Framework in Java - List",
#             "Collections Framework in Java - LinkedList",
#             "Collections Framework in Java - Queue",
#             "Collections Framework in Java - ArrayList",
#             "Uses and Applications of Collections",
#             "Data Structures in Java JShell",
#             "Garbage Collection"
#         ],
#         "experiential_learning": [
#             "Programs on Access Specifiers",
#             "Exception Handling",
#             "JShell Scripting",
#             "Multithreading",
#             "Java Collections Framework",
#             "Implementing Data Structures in Java"
#         ]
#         },
#         "unit_3": {
#         "title": "Web Application Development with Java",
#         "topics": [
#             "Introduction to JSP",
#             "Scriptlets",
#             "Expressions",
#             "Declarations",
#             "Database Management - SQL and NoSQL Databases",
#             "Database Management - Database Connectivity in Java with SQLite",
#             "Understanding JDBC",
#             "JDBC Classes and Interfaces - Connection",
#             "JDBC Classes and Interfaces - DriverManager",
#             "JDBC Classes and Interfaces - Statement",
#             "JDBC Classes and Interfaces - PreparedStatement",
#             "JDBC Classes and Interfaces - CallableStatement",
#             "JDBC Classes and Interfaces - ResultSet",
#             "MongoDB Operations in Java"
#         ],
#         "experiential_learning": [
#             "Developing Database Web Application using JSP and SQLite",
#             "Developing Database Web Application using JSP and MongoDB"
#         ]
#         },
#         "unit_4": {
#         "title": "Java Bean and Hibernate",
#         "topics": [
#             "Java Bean - Introduction",
#             "Java Bean - Bean Development",
#             "Java Bean - Introspection",
#             "Java Bean - Design Patterns of Java Beans",
#             "Java Bean - Simple Properties",
#             "Java Bean - Indexed Properties",
#             "Java Bean - BeanInfo",
#             "Java Bean - Persistence",
#             "Java Bean - JavaBeans API",
#             "Hibernate - Introduction",
#             "Hibernate - Architecture",
#             "Hibernate - Java Objects in Hibernate",
#             "Hibernate - Inheritance Mapping",
#             "Hibernate - Hibernate Query Language (HQL)",
#             "Hibernate - Hibernate Named Query",
#             "Hibernate - Associations and Relationships in ORM"
#         ],
#         "experiential_learning": [
#             "Java Bean Development",
#             "Application Development using Hibernate Framework"
#         ]
#         }
#     }
#     }
# ]
# pdf_bytes = combine_syllabi_pdfs(syllabi)

# # Save for testing (Optional)
# with open("combined_syllabi.pdf", "wb") as f:
#     f.write(pdf_bytes)

// creating an array and passing the number, questions, options, and answers
let questions = [
    {
    numb: 1,
    question: " Which of the following option leads to the portability and security of Java?",
    answer: "Bytecode is executed by JVM",
    options: [
      "Bytecode is executed by JVM",
      "Use of exception handling",
      "The applet makes the Java code secure and portable",
      "Dynamic binding between objects"
    ]
  },
    {
    numb: 2,
    question: "Which of the following is not a Java features?",
    answer: "Use of pointers",
    options: [
      "Dynamic",
      "Architecture Neutral",
      "Object-Oriented",
      "Use of pointers"
    ]
  },
    {
    numb: 3,
    question: " _____ is used to find and fix bugs in the Java programs.",
    answer: "JDB",
    options: [
      "JDB",
      "JDK",
      "JVM",
      "JRE"
    ]
  },
    {
    numb: 4,
    question: " Which of the following is a valid declaration of a char?",
    answer: "char ch = 'tea';",
    options: [
      "char cr = 102;",
      "char ch = 'tea';",
      "char cr = 425;",
      "char cc = '\itea';"
    ]
  },
    {
    numb: 5,
    question:  "Evaluate the following Java expression, if x=3, y=5, and z=10:++z + y - y + z + x++" ,
    answer: "25",
    options: [
      "20",
      "23",
      "24",
      "25",
  
      
    ]
  },
  {
    numb: 6,
    question: "  Which of the following for loop declaration is not valid?" ,
    answer: "for ( int i = 99; i >= 0; i / 9 )",
    options: [
      "for ( int i = 99; i >= 0; i / 9 )",
      "for ( int i = 20; i >= 2; - -i )",
      "for ( int i = 7; i <= 77; i += 7 )",
      "for ( int i = 2; i <= 20; i = 2* i )"
    ]
  },
  {
    numb: 7,
    question: " Out of these statements, which ones are incorrect?" ,
    answer: "The division operator / has comparatively higher precedence as compared to a multiplication operator",
    options: [
      "The addition operator + and the subtraction operator : have an equal precedence",
      "The division operator / has comparatively higher precedence as compared to a multiplication operator",
      "The Brackets () have the highest precedence",
      "The addition operator + and the subtraction operator : have an equal precedence"
    ]
  },
  
  {
    numb: 8,
    question: " Which statement is true about Java?" ,
    answer: " Java is a platform-independent programming language",
    options: [
      " Java is a code dependent programming language",
      " Java is a sequence-dependent programming language",
      "Java is a platform-dependent programming language",
      "Java is a platform-independent programming language"
    ]
  },
  
  {
    numb: 9,
    question: "Which of these cannot be used for a variable name in Java? " ,
    answer: "keyword",
    options: [
      "identifier",
      "identifier & keyword",
      "keyword",
      "None Of the above"
    ]
  },
  {
    numb: 10,
    question: " What is the extension of java code files?" ,
    answer: "	.java    ",
    options: [
      "	.java",
      ".class",
      ".js",
      ".txt"
    ]
  },
  
  
  
  // you can uncomment the below codes and make duplicate as more as you want to add question
  // but remember you need to give the numb value serialize like 1,2,3,5,6,7,8,9.....
  
  //   {
  //   numb: 6,
  //   question: "Your Question is Here",
  //   answer: "Correct answer of the question is here",
  //   options: [
  //     "Option 1",
  //     "option 2",
  //     "option 3",
  //     "option 4"
  //   ]
  // },
  ];
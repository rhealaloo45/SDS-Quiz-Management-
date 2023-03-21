// creating an array and passing the number, questions, options, and answers
let questions = [
    {
    numb: 1,
    question: "A tree is composed of ____ connected by edges or lines.",
    answer: "Nodes",
    options: [
      "Fruit",
      "Leaf Node",
      "Root node",
      "Nodes"
    ]
  },
    {
    numb: 2,
    question: "A Kind of tree where every node in a tree can have at most two children.",
    answer: "Binary Tree",
    options: [
      "Binary Tree",
      "Binary Search Tree",
      "Binary Expression Tree",
      "None of the above"
    ]
  },
    {
    numb: 3,
    question: "In preorder traversal of a binary tree the second step is ____________",
    answer: "Traverse the left subtree",
    options: [
      "Traverse the right subtree",
      "Traverse the left subtree",
      "Traverse right subtree and visit the root",
      "Visit the root"
    ]
  },
    {
    numb: 4,
    question: "The following numbers are inserted into an empty binary tree and binary search tree in the given order: 20,10, 1, 3, 5, 15, 12, 16,34,87,35. The height of the binary tree and binary search tree, respectively, is  ",
    answer: "(3,4)",
    options: [
      "(4,4)",
      "(3,3)",
      "(3,4)",
      "(4,3)"
    ]
  },
    {
    numb: 5,
    question: " The preorder traversal sequence of a binary search tree is 30, 20, 10, 15, 25, 23, 39, 35, 42. Which one of the following is the postorder traversal sequence of the same tree? " ,
    answer: "15, 10, 23, 25, 20, 35, 42, 39, 30",
    options: [
      "10, 20, 15, 23, 25, 35, 42, 39, 30",
      "15, 10, 25, 23, 20, 42, 35, 39, 30",
      "15, 20, 10, 23, 25, 42, 35, 39, 30",
      "15, 10, 23, 25, 20, 35, 42, 39, 30"
    ]
  },
  {
    numb: 6,
    question: " When you construct a BST with the preorder traversal of a binary search tree 10, 4, 3, 5, 11, 12,21,36, then which of the following are leaf nodes?" ,
    answer: "3,5,36",
    options: [
      "5,3,4",
      "5,3,12",
      "3,5,36",
      "None Of the above"
    ]
  },
  {
    numb: 7,
    question: " A tree with n vertices, consists of______ edges" ,
    answer: "n-1",
    options: [
      "n-1",
      "n-2",
      "n",
      "log n"
    ]
  },
  
  {
    numb: 8,
    question: " select one FALSE statement about binary trees" ,
    answer: "Every binary tree has atleast one node",
    options: [
      "Every non empty tree has exactly one root node",
      "Every node has atmost two children",
      "Every binary tree has atleast one node",
      "Every non root node has exactly one parent"
    ]
  },
  
  {
    numb: 9,
    question: "Which tree traversal visits root node last " ,
    answer: "postorder",
    options: [
      "inorder",
      "postorder",
      "preorder",
      "None Of the above"
    ]
  },
  {
    numb: 10,
    question: " What is the worst case time complexity for search, insert and delete operations in a general Binary Search Tree?" ,
    answer: "	O(n) for all",
    options: [
      "	O(n) for all",
      "O(Logn) for all",
      "O(Logn) for search and insert, and O(n) for delete",
      "O(Logn) for search, and O(n) for insert and delete"
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
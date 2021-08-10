const todos = [
    {
        id: 1,
        text: 'Take out trash',
        isCompleted: true
    },
    {
        id: 2,
        text: 'Meeting with boss',
        isCompleted: true
    },
    {
        id: 3,
        text: 'Destist appt',
        isCompleted: false
    }
    
];

//forEach, mao, filter
todos.forEach(function(todo) {
    console.log(todo.text)
});

const todoText = todos.map(function(todo) {
    return todo.text;
});

console.log(todoText)

const todoCompleted = todos.filter(function(todo) {
    return todo.isCompleted === true;
}).map(function(todo) {
    return todo.text;
})

console.log(todoCompleted);


const person = {
    firstName:'John',
    lastName: 'Doe',
    age: 30,
    hobbies: ['music', 'movies', 'sports'],
    address: {
        street: '50 mais st',
        city: 'Boston',
        state: 'MA',
    }

}

person.email = 'john@gmail.com'

console.log(person)

console.log(person.firstName, person.lastName);
console.log(person.hobbies[1], person.address.city);



const { firstName, lastName, address: { city}} = person;

console.log(city)



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

const todoJSON =JSON.stringify(todos);
console.log(todoJSON);
console.log(todos[1].text);


for(let todo of todos) {
    console.log(todo.text)
}


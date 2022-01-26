async function resolvePromise() {
    const myPromise = new Promise((resolve, reject) => {
        window.setTimeout(() => {
            resolve("Resolvida");
        }, 2000);
    });

    const resolved = await myPromise
        .then((result) => result + " passando pelo then")
        .then((result) => result + " e agora acabou")
        .catch((err) => console.log(err.message));

    return resolved;
}
await resolvePromise()

// Creating a new Promise and saving it to the testLuck variable. Two arguments are being passed, one for when the promise resolves, and one for if the promise gets rejected.
const testLuck = new Promise((resolve, reject) => {
    if (Math.random() < 0.5) { 
      resolve('Lucky winner!')
    } else {
      reject(new Error('Unlucky!'))
    }
  });
   
  testLuck.then(message => {
    console.log(message) // Log the resolved value of the Promise
  }).catch(error => {
    console.error(error) // Log the rejected error of the Promise
  });

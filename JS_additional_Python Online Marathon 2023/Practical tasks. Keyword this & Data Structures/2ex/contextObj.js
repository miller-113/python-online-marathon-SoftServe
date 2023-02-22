// The product() function finds the product of an arbitrary number of arguments. You must specify the desired execution context for the product() function by implementing a new getProduct() function bound to the context of the object, which takes 2 additional arguments.
//
//     The value of the 1st additional parameter is 2, the value of the 2nd additional parameter is 3. The object in the context of which the product() function is called has 1 property.
//
//
//
//     Context 2 task image
// * For correct passing of all tests don't use console.log() method in your code.


const product = function () {
    return [].reduce.call(arguments, function (res, elem) {
        return res * elem;
    }, 10);
};

const contextObj = {} // your code }

const getProduct = function (...args) {
    return product(2, 3, ...args)
}


// product function that is called in the context of an contextObj
// with two additional parameters
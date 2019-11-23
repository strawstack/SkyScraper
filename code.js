// [+]TAG
// n - an integer
// returns the factorial of n
function fact(n) {
    if n == 1: return 1;
    return n * fact(n - 1);
}
// [-]TAG

// [+]B
// the main routine
// called on document load
function main() {
    let a = 2 + 1;
    let f = fact(5);
    console.log("hello:" + f);
}
// [-]B

// [+]ANYTHING
// Call main when the document loads
window.onload = main;
// [-]ANYTHING

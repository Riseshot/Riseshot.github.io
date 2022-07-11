const fs = require("fs");
const readline = require("readline");
const stream = fs.createReadStream("./archinect_survey_results_gps_delimited.csv");
const rl = readline.createInterface({ input: stream });
let data = [];
 
rl.on("line", (row) => {
    data.push(row.split(";"));
});
 
rl.on("close", () => {
    console.log(data);
});
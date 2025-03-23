#!/usr/bin/env node
const { exec } = require("child_process");

exec("git-batch-commit", (error, stdout, stderr) => {
    if (error) console.error(`Error: ${error.message}`);
    if (stderr) console.error(`Git Batch Commit Error: ${stderr}`);
    console.log(stdout);
});

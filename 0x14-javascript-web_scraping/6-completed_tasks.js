const request = require('request');

const url = process.argv[2];

request(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else if (res.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completed = {};

    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ', +res.statusCode);
  }
});

#!/usr/bin/node
// script that prints the star wars movie

const request = require('request');
const id = process.argv[2];
const Api = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(Api, async function (err, res, body) {
  const getres = JSON.parse(body);

  if (err) {
    console.log(err);
  } else {
    for (const results of getres.characters) {
      await new Promise((resolve, reject) => {
        request(results, function (err, res, body2) {
          if (res) {
            const characterName = JSON.parse(body2);
            console.log(characterName.name);
            resolve();
          } else {
            console.log(err);
            reject(err);
          }
        });
      });
    }
  }
});

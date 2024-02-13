#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.height = w;
      this.width = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let string = '';
      for (let j = 0; j < this.width; j++) {
        string += 'X';
      }

      console.log(string);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}

module.exports = Rectangle;

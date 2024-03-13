#!/usr/bin/node
class Rectangle {
        constructor(w, h){
                if(w > 0 && h > 0){
                        this.width = w;
                        this.height = h;
        }
        }
	print () {
        for (let k = 0; k < this.width; k++){
	  let r = '';
          for (let m = 0; m < this.height; m++){
		r += 'X';
	    }
	    console.log(r);
	}
	}
}
module.exports = Rectangle;

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
            for (let m = 0; m < this.height; m++)
        console.log('x'.repeat(this.width), this.height);
	 }
	}
}
module.exports = Rectangle;

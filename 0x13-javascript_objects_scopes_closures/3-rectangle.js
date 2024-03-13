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
		 let a = '';
            for (let m = 0; m < this.height; m++){
		    a += 'x';
	    }
		 console.log(a);
         
	 }
	}
}
module.exports = Rectangle;

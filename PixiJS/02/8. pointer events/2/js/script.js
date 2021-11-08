let app
let r1
let r2
let r3

let pointerIsDown = false
let pointerIsOver = false
const NORMAL = 0xffffff
const OVER = 0x00ff00
const DOWN = 0xff0000
const RECT_W = 100
const RECT_H = 100

window.onload = function() {
    app = new PIXI.Application({
        width: 800,
        height: 600,
        backgroundColor: 0xAAAAAA
    })
    document.querySelector('#gameDiv').appendChild(app.view)

	r1 = createRect(100, 450, RECT_W, RECT_H, "rect01", 20)
	r2 = createRect(300, 450, RECT_W, RECT_H, "rect02", 40)
	r3 = createRect(500, 450, RECT_W, RECT_H, "rect03", 80)

	app.stage.addChild(r1)
	app.stage.addChild(r2)
	app.stage.addChild(r3)

    app.ticker.add(gameLoop)
    
}

function gameLoop(delta) {

}

function createRect(x,y,w,h,name,speed) {
	let rect = new PIXI.Graphics()

    rect.beginFill(NORMAL)
    rect.drawRect(x, y, w, h)
    rect.endFill()
    rect.interactive = true
    rect.buttonMode = true

    rect.on('pointerup', doPointerUp)
    rect.on('pointerdown', doPointerDown)
    rect.on('pointerover', doPointerOver)
    rect.on("pointerout", doPointerOut)
    rect.on("pointerupoutside", doPointerUpOutside)

	rect.name = name
	rect.speed = speed

	return rect
}

function doPointerUp() {
    if (pointerIsOver) {
        this.tint = NORMAL
		this.y = this.y - this.speed
		console.log("moving -> " + this.name)
    } else {
        this.tint = OVER       
    }
    pointerIsDown = false
}

function doPointerDown() {
    this.tint = DOWN
    pointerIsDown = true
}

  function doPointerOver() {
    if (!pointerIsDown) {
      this.tint = OVER
      pointerIsOver = true
    }
  }
  

  function doPointerOut() {
    pointerIsOver = false
    if (!pointerIsDown) {
      this.tint = NORMAL
    }
  }

  function doPointerUpOutside() {
    this.tint = NORMAL;
    pointerIsOver = false
    pointerIsDown = false
  }


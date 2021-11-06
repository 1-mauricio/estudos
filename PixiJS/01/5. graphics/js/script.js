const canvas = document.getElementById('mycanvas');

const app = new PIXI.Application({
    view: canvas,
    width: window.innerWidth, 
    height: window.innerHeight
});

let graphic = new PIXI.Graphics()
graphic.x = app.renderer.width / 2
graphic.y = app.renderer.height / 2
app.stage.addChild(graphic)

let radius = 50

//graphic.lineStyle(5, 0x00ff00)
graphic.beginFill(0xff0000)
//graphic.drawCircle(0,0,100) //circulo
//graphic.drawRect(0,0,100,200) //retangulo
//graphic.drawStar(0,0,5,100,40) //estrela
//graphic.drawShape(new PIXI.Circle(0,0,10))
//graphic.drawPolygon(new PIXI.Point(100,100), new PIXI.Point(100,200), new PIXI.Point(200,100) )
//graphic.closePath()

/*
graphic.moveTo(0,0)
graphic.lineTo(100,100)
graphic.lineTo(100,200)
graphic.lineTo(0,200)
graphic.bezierCurveTo(-200,200,-200,100,-100,0)
graphic.quadraticCurveTo(-200,-100,0,-200)
graphic.arc(0,0,50,0,1)
*/
graphic.arc(0,0,radius,0,Math.PI*2) //circle
graphic.endFill()

app.ticker.add(animate);

let delta = 0

function animate() {
    delta += 0.1
    radius = 50 + Math.sin(delta) *25

    graphic.clear()
    graphic.beginFill(0xff0000)
    graphic.arc(0,0,radius,0,Math.PI*2) //circle
    graphic.endFill()

}
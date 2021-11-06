const canvas = document.getElementById('mycanvas')

/*
const app = new PIXI.Application({
    view: canvas,
    width: window.innerWidth,
    height: window.innerHeight
})
*/

// FULL SCREEN
//document.body.appendChild(app.view) 

let _w = window.innerWidth
let _h = window.innerHeight


const renderer = new PIXI.Renderer({
    view: canvas,
    width: _w,
    height: _h,
    resolution: window.devicePixelRatio,
    autoDensity: true

})

window.addEventListener('resize', resize)

function resize() {
    _w = window.innerWidth
    _h = window.innerHeight

    renderer.resize(_w, _h)
}

const stage = new PIXI.Container()

const texture = PIXI.Texture.from('sprite.png')
const img = new PIXI.Sprite(texture)
const img2 = new PIXI.Sprite(texture)
//img.x = app.renderer.width / 2
//img.y = app.renderer.height / 2

img.anchor.x = 0.5
img.anchor.y = 0.5
//app.stage.addChild(img)
stage.addChild(img)

//app.ticker.add(animate)
const ticker = new PIXI.Ticker()
ticker.add(animate)
ticker.start()

function animate() {
    img.x = renderer.screen.width / 2
    img.y = renderer.screen.height / 2
    img.rotation += 0.05
    renderer.render(stage)
}
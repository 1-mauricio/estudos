const canvas = document.getElementById('mycanvas')

const app = new PIXI.Application({
    view: canvas,
    width: window.innerWidth, 
    height: window.innerHeight
})

const texture = PIXI.Texture.from('sprite2.png')
const texture2 = PIXI.Texture.from('sprite.png')

let sprite1,
    sprite2,
    sprite3

img = new PIXI.Sprite(texture)
img.x = app.renderer.width / 2
img.y = app.renderer.height / 2
img.anchor.x = 0.5
img.anchor.y = 0.5
app.stage.addChild(img)

let container = new PIXI.Container()
app.stage.addChild(container)

/*
sprite1 = new PIXI.Sprite(texture2)
sprite1.position.set(app.renderer.screen.width / 2, app.renderer.screen.height / 2)
sprite1.anchor.set(0.5)
container.addChild(sprite1)

sprite2 = new PIXI.Sprite(texture2)
sprite2.x = 100
sprite2.y = 100
sprite2.tint = 0xff0000 //cor
container.addChild(sprite2)

sprite3 = new PIXI.Sprite(texture2)
//sprite3.x = 200
//sprite3.y = 100
sprite3.position.set(200,100) // posição
sprite3.anchor.set(0.5) // ponto central
sprite3.pivot.set(100,100) //ponto de rotação
container.addChild(sprite3)
*/

let sprites = []

addSprites()

app.ticker.add(anaaimate)

function addSprites() {
    for (let i = 0; i < 10; i++) {
        let sprite = new PIXI.Sprite(texture2) 
        sprite.x = Math.random() * app.renderer.screen.width
        sprite.y = Math.random() * app.renderer.screen.height
        sprite.tint = Math.random() * 0xffffff
        sprite.anchor.set(0.5)
    
        container.addChild(sprite)
        sprites.push(sprite)
    }
}
let delta = 0

function animate() {
    delta += 0.1

    container.y  = Math.sin(delta) * 10

    for (let i = 0; i < sprites.length; i++) {
        sprites[i].rotation += 0.1
    }


    /*
    //sprite1.y = 100 + Math.sin(delta) * 10 //eixo y
    sprite2.x = 100 + Math.sin(delta) * 10 //eixo x
    sprite3.scale = new PIXI.Point(2,2) //size
    sprite3.rotation += 0.1 //rotation
    //sprite1.alpha = Math.sin(delta) //opacity
    sprite1.blendMode = PIXI.BLEND_MODES.MULTIPLY // white to transparent
    //sprite1.visible = false // invisible
    
    /*
    sprite1.interactive = true
    sprite1.buttonMode = true
    */

    
}
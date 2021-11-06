let app
let player
let keys = {}
let keysDiv

window.onload = function() {
    app = new PIXI.Application({
        width: 800,
        width: 600,
        backgroundColor: 0xAAAAAA
    })

    document.body.appendChild(app.view)

    //player object
    graphic = new PIXI.Graphics()

    graphic.beginFill(0xFFFF00)
    graphic.drawRect(0,0,50, 50) 
    graphic.closePath()
    graphic.endFill()

    let texture = renderer.generateTexture(graphic)
    let player = new PIXI.Sprite(texture)

    player.x = app.view.width / 2
    player.y = app.view.height / 2
    player.anchor.set(0.5)

    app.stage.addChild(player)
    

    // keyboard event handlers
    window.addEventListener('keydown', keysDown)
    window.addEventListener('keyup', keysUp)

    app.ticker.add(gameLoop)

    keysDiv = document.querySelector('#keys')
}

function keysDown(e) {
    keys[e.keyCode] = true
}

function keysUp(e) {
    keys[e.keyCode] = false
}

function gameLoop() {
    keysDiv.innerHTML = JSON.stringify(keys)
    // dir
    if (keys["39"]) {
        player.x += 5
    }
    // esq
    if (keys["37"]) {
        player.x -= 5
    }
    // cima
    if (keys["38"]) {
        player.y -= 5
    }

    //baixo
    if (keys["40"]) {
        player.y += 5
    }
}

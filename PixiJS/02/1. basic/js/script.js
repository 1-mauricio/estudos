let app
let player

window.onload = function() {
    app = new PIXI.Application({
        width: 800,
        width: 600,
        backgroundColor: 0xAAAAAA
    })

    document.body.appendChild(app.view)

    //player object
    player = new PIXI.Graphics()
    player.x = app.view.width / 2
    player.y = app.view.height / 2
    app.stage.addChild(player)

    player.beginFill(0xFFFF00)
    player.drawRect(0,0,50, 50) //retangulo
    player.closePath()
    player.endFill()
    

    // mouse interactions

    app.stage.interactive = true
    app.stage.on('pointermove', movePlayer)

}

function movePlayer (e) {
    let pos = e.data.global
    
    player.x = pos.x
    player.y = pos.y
}
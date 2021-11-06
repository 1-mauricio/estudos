let app
let player
let bloats = {}

window.onload = function() {
    app = new PIXI.Application({
        width: 800,
        width: 600,
        backgroundColor: 0xAAAAAA
    })

    document.body.appendChild(app.view)

    for (let i = 0; i < 10; i++) {
        player = new PIXI.Graphics()
        player.x = app.view.width / 2
        player.y = app.view.height / 2
        app.stage.addChild(player)
        
        player.beginFill(0xFFFF00)
        player.drawRect(0,0,50, 50) 
        player.closePath()
        player.endFill()
        
    }

}



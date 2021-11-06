
let app
let speed = 4


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

    let texture = app.renderer.generateTexture(graphic)
    let player = new PIXI.Sprite(texture)
    let enemy = new PIXI.Sprite(texture)

    player.anchor.set(0.5)
    player.x = 16
    player.y = app.view.height / 2
    app.stage.addChild(player)


    enemy.anchor.set(0.5)
    enemy.x = app.view.width - 16
    enemy.y = app.view.height / 2
    app.stage.addChild(enemy)

    app.ticker.add(gameLoop)
    

    // keyboard event handlers
    function gameLoop(delta) {
        player.x += speed
        enemy.x -= speed

        if (rectsIntersect(player, enemy)) {
            speed = 0
        }
    }
    
    function rectsIntersect(a, b) {
        let aBox = a.getBounds()
        let bBox = b.getBounds()

        return aBox.x + aBox.width > bBox.x && 
                aBox.x < bBox.x + bBox.width &&
                aBox.y + aBox.height > bBox.y &&
                aBox.y < bBox.y + bBox.height
    }
}




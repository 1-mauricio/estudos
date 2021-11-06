const canvas = document.getElementById('mycanvas');

const app = new PIXI.Application({
    view: canvas,
    width: window.innerWidth, 
    height: window.innerHeight
});

console.log(PIXI.utils.TextureCache)

let loader = PIXI.Loader.shared


loader.onComplete.add(handleLoadComplete)
loader.onLoad.add(handleLoadAsset)
loader.onError.add(handleLoadError)
loader.onProgress.add(handleLoadProgress)

loader.add('guy', 'sprite.png')
loader.add('bg', 'sprite2.png')
loader.load()

/*
loader.add('sprite.png')
    .on("progress", handleLoadProgress)
    .on('load', handleLoadAsset)
    .on('error', handleLoadError)
    .load(handleLoadComplete)

*/
let img;

function handleLoadProgress(loader, resource) {
    console.log(loader.progress + '% loaded')
}

function handleLoadAsset(loader, resource) {
    console.log('asset loaded ' + resource.name)
}

function handleLoadError() {
    console.error('load error')
}

function handleLoadComplete() {
    let texture = loader.resources.guy.texture
    img = new PIXI.Sprite(texture)
    img.anchor.x = 0.5
    img.anchor.y = 0.5
    app.stage.addChild(img)

    img.x = app.renderer.screen.width / 2
    img.y = app.renderer.screen.height / 2

    img.interactive = true
    img.buttonMode = true

    img.on('pointerdown', app.ticker.add(animate))
}

function change(){
    setTimeout(() => {
        img.texture = loader.resources.bg.texture
    }, 2000)
}

function animate() {
    
    img.rotation += 0.1;
}
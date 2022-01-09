var canvas = document.getElementById('headlinelogocanvas');
var container = document.querySelector('.headlinelogo')
document.addEventListener('mousemove', onMouseMove, false);
var mouseX;
var mouseY;
const aspect = container.clientWidth / container.clientHeight;
// console.log(container);
// console.log(headlinelogocanvas)
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(70, aspect, 0.1, 1000);



var renderer = new THREE.WebGLRenderer({ canvas: headlinelogocanvas, antialias: true, alpha: true });
// renderer.outputEncoding = THREE.sRGBEncoding;

// Light
scene.add(new THREE.AmbientLight(0x404040, 1));

var light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(-6, 3, 8);
scene.add(light);


var geometry = new THREE.SphereGeometry(2.15, 32, 32);
// var texture = new new THREE.TextureLoader().load('../images/EarthTexture.png')
var texture = new new THREE.TextureLoader().load('../static/images/textures/earthtexture2.3.1.jpg')
var material = new THREE.MeshPhongMaterial({
    map: texture,
    bumpMap: new THREE.TextureLoader('../static/images/textures/elev_bump_4k.jpg'),
    bumpScale: 0.005,
    specularMap: new THREE.TextureLoader('../static/images/textures/water_4k.png'),
    specular: new THREE.Color('grey')
});
var sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);

camera.position.z = 5;
var animate = function() {
    requestAnimationFrame(animate);
    // sphere.rotation.x += 0.001;
    // sphere.rotation.z += 0.01;
    sphere.rotation.y += 0.01;

    renderer.render(scene, camera);
};
var myTween;

function onMouseMove(event) {
    if (myTween)
        myTween.kill();

    mouseX = (event.clientX / window.innerWidth) * 2 - 1;
    mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
    myTween = gsap.to(sphere.rotation, { duration: 0.5, x: mouseY * -1, y: mouseX * 4 });
    //particles.rotation.x = mouseY*-1;
    //particles.rotation.y = mouseX;
}
animate();
from django.conf import settings


def get_pwa_config():
	DEFAULT_CONFIG = {
		"name": "Escrow Teller",
		"short_name": "Escrow Teller",
		"theme_color": "#7820f5",
		"background_color": "#7820f5",
		"display": "standalone",
		"orientation": "any",
		"scope": "/",
		"start_url": "/",
		"icons": [
			{
				"src": "/static/pwa/images/icons/72x72.png",
				"type": "image/png",
				"sizes": "72x72"
			},
			{
				"src": "/static/pwa/images/icons/96x96.png",
				"type": "image/png",
				"sizes": "96x96"
			},
			{
				"src": "/static/pwa/images/icons/128x128.png",
				"type": "image/png",
				"sizes": "128x128"
			},
			{
				"src": "/static/pwa/images/icons/144x144.png",
				"type": "image/png",
				"sizes": "144x144"
			},
			{
				"src": "/static/pwa/images/icons/152x152.png",
				"type": "image/png",
				"sizes": "152x152"
			},
			{
				"src": "/static/pwa/images/icons/192x192.png",
				"type": "image/png",
				"sizes": "192x192"
			},
			{
				"src": "/static/pwa/images/icons/384x384.png",
				"type": "image/png",
				"sizes": "384x384"
			},
			{
				"src": "/static/pwa/images/icons/512x512.png",
				"type": "image/png",
				"sizes": "512x512"
			}
		],
		"lang": "en",
		"dir": "ltr",
		"description": "Blockchain Payment, Data Management & Security Service",
        "version": "1.",
        "manifest_version": "1.0",
		"permissions": [
			"notifications",
			"webRequest"
		],
		"author": "Escrow Teller Team"
		}
	try:
		if settings.PWA_CONFIG and settings.PWA_CONFIG != {}:
			return settings.PWA_CONFIG
	except:
		return DEFAULT_CONFIG



def get_service_worker():
	SERVICE_WORKER = """
	var CACHE_NAME = 'pwa-cache-v1';
	var urlsToCache = [
		'/',
		'/sw.js',
		'/app.js',
		'/manifest.json',
		'/offline',
		'/static/pwa/images/dino.gif',

		'/static/js/bootstrap.min.css',
		'/static/js/popper.min.js',
		'/static/js/bootstrap.min.js',
		'/static/css/vendor-bundle.css',
		'/static/css/style-azure.css',
		'/static/css/font-awesome-5.13.0.css',
		'/static/css/font-awesome-4.7.0.css',
		'/static/css/smooth-scrow.css',
		'/static/css/back-to-top.css',
		'/static/js/jquery.min.js',
		'/static/js/angular.js',
		'/static/js/jquery-bundle.js',
		'/static/js/scripts.js',
		'/static/js/back-to-top.js',
		'/static/js/bg_particles.js',
		'/static/js/smooth_page_scroll.js',
		'/static/js/jquery.collapser.js',

		];
	const self = this;
	
	// Install SW
	self.addEventListener('install', (event) =>{
		event.waitUntil(
			caches.open(CACHE_NAME)
				.then((cache) => {
					console.log('Opend Cache.');
					
					return cache.addAll(urlsToCache);
				})
			)
	});

	// Listen For requests
	self.addEventListener('fetch', (event) =>{
		event.respondWith(
			caches.match(event.request)
				.then(() => {
					return fetch(event.request)
						.catch(() => caches.match('/offline'))
				})
		)
	});

	// Activate
	self.addEventListener('activate', (event) =>{
		const cacheWhitelist = [];
		cacheWhitelist.push(CACHE_NAME);
	 	event.waitUntil(
			caches.keys().then((cacheNames) => Promise.all(
				cacheNames.map((cacheName) => {
					if (!cacheWhitelist.includes(cacheName)) {
						return caches.delete(cacheName);
						}
					})
				))
			)
	});
	"""
	try:
		if settings.PWA_SW and settings.PWA_SW != {}:
			return settings.PWA_SW
	except:
		return SERVICE_WORKER


def get_app():
	APP = """
	if ("serviceWorker" in navigator) {
		window.addEventListener("load", () => {
			navigator.serviceWorker
			.register("/sw.js")
			.then(res => console.log("service worker registered!"))
			.catch(err => console.log("Your browser support service worker but service worker not registered.", err));
			});
		} else {
			console.log(`Your browser Dosn't Support serviceWorker, so you can'n install PWA.`);
		};
	"""
	try:
		if settings.PWA_APP and settings.PWA_APP != {}:
			return settings.PWA_APP
	except:
		return APP



screens = {
	'Chrome': {
		'Default CA/cert': [
			'certcheck_chromium_msauthority01.png'
			],
		'Default CA, similar cert': [
			'certcheck_chromium_mrsimillar01.png'
			],
		'Similar CA, similar cert': [
			'certcheck_chromium_simillarjunior01.png'
			],
		'Self-signed cert': [
			'certcheck_chromium_drselfsigned01.png', 'certcheck_chromium_drselfsigned02.png',
			'certcheck_chromium_drselfsigned03.png',
			'certcheck_chromium_drselfsigned04.png'
			],
		'Faked cert and CA': [
			'certcheck_chromium_unknownvalid01.png',
			'certcheck_chromium_unknownvalid02.png',
			'certcheck_chromium_unknownvalid03.png',
			'certcheck_chromium_unknownvalid04.png'
			],
		'A valid but untrusted CA, real cert': [
			'certcheck_chromium_jackmiddleattacer01.png',
			'certcheck_chromium_jackmiddleattacer02.png',
			'certcheck_chromium_jackmiddleattacer03.png',
			'certcheck_chromium_jackmiddleattacer04.png'
			]
		},
	'Firefox': {
		'Default CA/cert': [
		],
		'Default CA, similar cert': [
			'd2.png', 
			'sm2.png'		
			],
		'Similar CA, similar cert': [
			'd3.png', 
			'sm3.png'		
			],
		'Self-signed cert': [
			'd4.png', 
			'sm4.png'		
			],
		'Faked cert and CA': [
			'd5.png', 
			'sm5.png'		
			],
		'A valid but untrusted CA, real cert': [
			'd6.png', 
			'sm6.png'		
		]
	}
}
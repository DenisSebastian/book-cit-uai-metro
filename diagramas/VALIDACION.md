# Validación de diagramas

El libro publica **cinco SVG estáticos**: un flujo para cada bloque y un esquema de los tres enfoques de prevención. `svg_legibles.py` los regenera desde las especificaciones JSON de Archify con la misma paleta, tarjetas y flechas, en una disposición que permite rótulos de **15 a 20 px** al ancho del libro. Los pies de figura permanecen en los archivos `.qmd`.

Las cinco especificaciones pasaron la validación `showcase` de Archify con **9/9 comprobaciones**, sin errores ni advertencias de composición. El HTML interactivo `modelamiento.html` se actualizó con SHA-256 `1cf3a5b8bcbcdd8432080b9ccfb31e506cc626ce602e66787345789bd64a2240`. Su `visual-check` automatizado no pudo terminar porque Chrome cerró con `SIGABRT`; el visor no se incorpora al libro. La imagen estática `modelamiento.svg` sí se convirtió a PNG y se inspeccionó visualmente.

Los cinco SVG se analizaron como XML, se convirtieron a PNG con ImageMagick y se revisaron visualmente: los rótulos caben dentro de las tarjetas, las flechas muestran la secuencia o las rutas y la tipografía es legible. El libro se generó con Quarto sin errores.

| Figura SVG | SHA-256 |
|---|---|
| `enfoques.svg` | `1d07872b627d76b637cd0ad585edcf7caca1a35a374ac8f59f6ec70e4f93e6b0` |
| `datos.svg` | `c212d7492d11c4cdf199f87846b0c0298980a4325a49e49adf31de3fb80fdd4f` |
| `espacial.svg` | `00e83f57d8c7e945ba13dd46be0ee5cea165d79a33a81d64411d8022852e9a57` |
| `modelamiento.svg` | `3ce1bf1def5b49ab20c09affdceadc688311292875529760434e247101f5342f` |
| `tres-enfoques.svg` | `0620f69d8fafd2ef5bebaabe5895b03537eb4805d8bf9691c33c74d1faec99cd` |

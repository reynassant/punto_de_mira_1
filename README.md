# Practica 2 - Nuevas funcionalidades

El prototipo ha demostrado ser un éxito, parece que tiene potencial, pero aún hay que trabajar mucho para convertirlo en una idea divertida.

0. Bifurca (fork) el repositorio que encontrarás en: [https://github.com/elMestreAcademy/punto_de_mira_1](https://github.com/elMestreAcademy/punto_de_mira_1). El programa tiene dependencias indicadas en el fichero requirements.txt. Asegúrate de instalarlas en tu entorno antes de ejecutar el código.

1. El programa actualmente dispara una línea de balas para comprobar la desviación del arma. Actualmente las balas no se desvían ni un poquito. Modifica el programa de tal forma que cada bala se desvíe proporcionalmente con relación a su distancia del punto de mira (hipotenusa). Esta mecánica debería de añadir algo de interés a los tiroteos

2. Parece que el desvío funciona, pero parece demasiado exagerado. Tenemos que conseguir algo más gratificante para el usuario. Modifica la cadencia de tiro del arma (ROF) a 40 balas por segundo. Además, modifica la aleatorización de forma que dependa proporcionalmente de la constante RANDOM_FACTOR. Haz dos capturas de la ventana, una para RANDOM_FACTOR=1 y la segunda para RANDOM_FACTOR=0.25

3. Todos los pasos anteriores deben contar con su correspondientes commits en un repositorio. Asegúrate que sea público e indica la dirección donde se puede encontrar

4. **Bonus:** (Nota: Este apartado es para nota. Es más difícil, lleva más trabajo y está peor puntuado que los anteriores. Consejo: inténtalo solo después de comprobar todo el resto... y de tener una buena presentación)
Dibuja la secuencia de balas originales junto la desviada. Utiliza dos colores claramente diferenciados para cada secuencia

package org.formacion.factorymethod;

// clase base que usara el cliente para crear cualquier tipo de lavadora
public abstract class LavadoraFactory {
	
	
	// proceso de construccion comun
	public Lavadora crea() {
		
		Lavadora lavadora = creaLavadora();
		
		lavadora.ponerMandos();
		lavadora.ponerTambor();
		
		return lavadora;
	}
	
	// proceso de construccion especifico de cada tipo de lavadora
	// Permite que el tipo devuelto sea un subtipo de Lavadora (y por tanto,
	//  las invocaciones al metodo crea() devuelvan tipos diferentes de lavadoras)
	protected abstract Lavadora creaLavadora();

}

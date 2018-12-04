package org.formacion.abstractfactory;

import static org.junit.Assert.*;

import org.junit.Test;

public class TestMultiIdioma {

	@Test
	public void test_es() {
		
		// unico punto de decision
		MensajesAbstractFactory factory = new MensajesEsFactory(); 
		
		Preguntas preguntas = factory.getPreguntas();
		
		assertEquals("¿qué hora es?", preguntas.preguntaHora() );
		assertEquals("¿qué tiempo hace?", preguntas.preguntaTiempo() );
		
		Saludos saludos = factory.getSaludos();
		
		assertEquals("buenos días", saludos.buenosDias());
		assertEquals("buenas tardes", saludos.buenasTardes());
	}
	
	@Test
	public void test_en() {

		// unico punto de decision
		MensajesAbstractFactory factory = new MensajesEnFactory(); 

		Preguntas preguntas = factory.getPreguntas();
		
		assertEquals("what time is it?", preguntas.preguntaHora() );
		assertEquals("how is the weather?", preguntas.preguntaTiempo() );
		
		Saludos saludos = factory.getSaludos();
		
		assertEquals("good morning", saludos.buenosDias());
		assertEquals("good afternoon", saludos.buenasTardes());
	}

}

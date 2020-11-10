package com.mycompany.unicafe;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MaksukorttiTest {

    Maksukortti kortti;

    @Before
    public void setUp() {
        kortti = new Maksukortti(1000);
    }

    @Test
    public void luotuKorttiOlemassa() {
        assertTrue(kortti!=null);      
    }
    
    @Test
    public void kortinSaldoOnOikein() {
        assertEquals(1000, kortti.saldo());
    }
    
    
    @Test
    public void saldoKasvaaOikein() {
        kortti.lataaRahaa(1000);
        assertEquals(2000, kortti.saldo());
    }
    
    @Test
    public void saldoEiMuutuJosSitaEiOleTarpeeksi() {
        kortti.otaRahaa(2000);
        assertEquals(1000, kortti.saldo());
    }
    
    @Test
    public void trueJosSaldoRiitti() {
        assertTrue(kortti.otaRahaa(1000));
    }
    
    @Test
    public void falseJosSaldoEiRiittanyt() {
        assertFalse(kortti.otaRahaa(2000));
    }
    
    
}

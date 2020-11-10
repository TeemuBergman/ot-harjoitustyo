package com.mycompany.unicafe;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class KassapaateTest {

    Maksukortti kortti;
    Kassapaate kassa;

    @Before
    public void setUp() {
        kortti = new Maksukortti(1000);
        kassa = new Kassapaate();
    }

    // KASSAN ALKUTILA
    @Test
    public void alussaKassassaOnOikeaSummaRahaa() {
        assertEquals(100000, kassa.kassassaRahaa());
    }

    @Test
    public void alussaEdullisiaLounaitaMyytyNolla() {
        assertEquals(0, kassa.edullisiaLounaitaMyyty());
    }

    @Test
    public void alussaMaukkaitaLounaitaMyytyNolla() {
        assertEquals(0, kassa.maukkaitaLounaitaMyyty());
    }

    // KÄTEISOSTON TESTIT
    @Test
    public void saldoKasvaaEdullisenLounaanVerranSekaVaihtorahaOnOikein() {
        assertEquals(260, kassa.syoEdullisesti(500));
        assertEquals(100240, kassa.kassassaRahaa());
    }

    @Test
    public void saldoKasvaaMaukkaanLounaanVerranSekaVaihtorahaOnOikein() {
        assertEquals(100, kassa.syoMaukkaasti(500));
        assertEquals(100400, kassa.kassassaRahaa());
    }

    @Test
    public void josMaksuOnRiittavaEdullistenLounaidenMaaraKasvaaYhteen() {
        kassa.syoEdullisesti(240);
        assertEquals(1, kassa.edullisiaLounaitaMyyty());
    }

    @Test
    public void josMaksuOnRiittavaMaukkaidenLounaidenMaaraKasvaaYhteen() {
        kassa.syoMaukkaasti(400);
        assertEquals(1, kassa.maukkaitaLounaitaMyyty());
    }

    @Test
    public void saldoJaMaaraEiKasvaEdullisestaLounaastaKunRahaaOnLiianVahanJaRahaPalautetaan() {
        assertEquals(100, kassa.syoEdullisesti(100));
        assertEquals(100000, kassa.kassassaRahaa());
        assertEquals(0, kassa.edullisiaLounaitaMyyty());
    }

    @Test
    public void saldoJaMaaraEiKasvaMaukkaastaLounaastaKunRahaaOnLiianVahanJaRahaPalautetaan() {
        assertEquals(100, kassa.syoMaukkaasti(100));
        assertEquals(100000, kassa.kassassaRahaa());
        assertEquals(0, kassa.maukkaitaLounaitaMyyty());
    }

    // KORTTIOSTON TESTIT
    @Test
    public void josKortillaOnSaldoaSyoEdullisestiPalauttaaTrue() {
        assertTrue(kassa.syoEdullisesti(kortti));
    }

    @Test
    public void josKortillaOnSaldoaSyoMaukkaastiPalauttaaTrue() {
        assertTrue(kassa.syoMaukkaasti(kortti));
    }

    @Test
    public void josKortillaOnSaldoaMyytyjenEdullistenLounaidenMääräKasvaaYhteen() {
        kassa.syoEdullisesti(kortti);
        assertEquals(1, kassa.edullisiaLounaitaMyyty());
    }

    @Test
    public void josKortillaOnSaldoaMyytyjenMaukkaidenLounaidenMääräKasvaaYhteen() {
        kassa.syoMaukkaasti(kortti);
        assertEquals(1, kassa.maukkaitaLounaitaMyyty());
    }

    @Test
    public void josKortillaEiOleSaldoaSyoEdullisestiPalauttaaFalseJaSaldotEivätMuutu() {
        kortti = new Maksukortti(100);
        assertFalse(kassa.syoEdullisesti(kortti));
        assertEquals("saldo: 1.0", kortti.toString());
        assertEquals(0, kassa.edullisiaLounaitaMyyty());
    }

    @Test
    public void josKortillaEiOleSaldoaSyoMaukkaastiPalauttaaFalseJaSaldotEivätMuutu() {
        kortti = new Maksukortti(100);
        assertFalse(kassa.syoMaukkaasti(kortti));
        assertEquals("saldo: 1.0", kortti.toString());
        assertEquals(0, kassa.maukkaitaLounaitaMyyty());
    }

    @Test
    public void kassanSaldoEiKasvaKunMaksetaanKortillaEdullinenLounas() {
        assertTrue(kassa.syoEdullisesti(kortti));
        assertEquals(100000, kassa.kassassaRahaa());
    }

    @Test
    public void kassanSaldoEiKasvaKunMaksetaanKortillaMaukasLounas() {
        assertTrue(kassa.syoMaukkaasti(kortti));
        assertEquals(100000, kassa.kassassaRahaa());
    }

    @Test
    public void kassanSaldoKasvaaKunKorttinSaldoaOstetaanLisaa() {
        kassa.lataaRahaaKortille(kortti, 1000);
        assertEquals(101000, kassa.kassassaRahaa());
    }

    @Test
    public void kassanSaldoEiKasvaKunKortilleYritetaanLisataNolla() {
        kassa.lataaRahaaKortille(kortti, -1);
        assertEquals(100000, kassa.kassassaRahaa());
    }
}

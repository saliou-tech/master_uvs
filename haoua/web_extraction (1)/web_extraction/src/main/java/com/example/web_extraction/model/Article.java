package com.example.web_extraction.model;

import org.springframework.data.mongodb.core.mapping.Document;

import java.util.ArrayList;
import java.util.List;

@Document(collection = "scraper_tb")
public class Article {

    private String id;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<List<String>> getCategorie() {
        return categorie;
    }

    public void setCategorie(List<List<String>> categorie) {
        this.categorie = categorie;
    }

    public List<List<String>> getUrl() {
        return url;
    }

    public void setUrl(List<List<String>> url) {
        this.url = url;
    }

    public List<List<String>> getTitre() {
        return titre;
    }

    public void setTitre(List<List<String>> titre) {
        this.titre = titre;
    }

    public List<List<String>> getTexte() {
        return texte;
    }

    public void setTexte(List<List<String>> texte) {
        this.texte = texte;
    }

    public List<List<String>> getAuteur() {
        return auteur;
    }

    public void setAuteur(List<List<String>> auteur) {
        this.auteur = auteur;
    }

    public List<List<String>> getPublication() {
        return publication;
    }

    public void setPublication(List<List<String>> publication) {
        this.publication = publication;
    }

    public List<List<String>> getVue() {
        return vue;
    }

    public void setVue(List<List<String>> vue) {
        this.vue = vue;
    }

    List<List<String>>   categorie;
    List<List<String>>   url;
    List<List<String>>   titre;
    List<List<String>>  texte;
    List<List<String>>   auteur;
    List<List<String>>   publication;
    List<List<String>>   vue;








}

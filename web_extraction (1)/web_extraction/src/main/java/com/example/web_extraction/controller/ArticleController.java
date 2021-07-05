package com.example.web_extraction.controller;


import com.example.web_extraction.model.Article;
import com.example.web_extraction.repository.ArticleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@CrossOrigin("*")
@RequestMapping(value = "/article")
public class ArticleController {
    @Autowired
    public  ArticleRepository articleRepository;
    @GetMapping(value = "/listAll")
    public List<Article> getAll(){
        List<Article> articles = null;
        try{
            articles=articleRepository.findAll();
        }catch (Exception e){
            e.printStackTrace();
        }
        return articles;
    }

}

package com.example.application_409;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // push test
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        Button Button_add = findViewById(R.id.button2);
        Button_add.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), RegisterActivity.class);
                startActivity(intent);
                // RegisterActivity로 이동
            }
        });
        Button Button_login = findViewById(R.id.button3);
        Button_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), LoginActivity.class);
                startActivity(intent);
                // LoginActivity로 이동
            }
        });
    }
}
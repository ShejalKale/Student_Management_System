
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  name = '';
  email = '';
  response: any;

  constructor(private http: HttpClient) {}

  submitForm() {
    const formData = new FormData();
    formData.append('name', this.name);
    formData.append('email', this.email);

    this.http.post('https://pythoncrud-hmb2cgh4b8dgfpf3.centralindia-01.azurewebsites.net/submit', formData)
      .subscribe({
        next: (res) => this.response = res,
        error: (err) => console.error('Error:', err)
      });
  }
}

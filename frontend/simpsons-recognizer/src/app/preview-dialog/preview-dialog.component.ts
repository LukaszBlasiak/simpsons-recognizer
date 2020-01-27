import {Component, Inject, OnInit} from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import {HttpClient, HttpParams} from '@angular/common/http';

@Component({
  selector: 'app-preview-dialog',
  templateUrl: './preview-dialog.component.html',
  styleUrls: ['./preview-dialog.component.sass']
})
export class PreviewDialogComponent implements OnInit {

  isLoading = false;
  imageAsBase64 = '';

  constructor(
    public dialogRef: MatDialogRef<PreviewDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data,
    private http: HttpClient) {
  }

  ngOnInit() {
    this.isLoading = true;
    this.http.post('http://localhost:8080/api/image', this.data).subscribe(
      id => {
        this.getProcessedImage(id, 1);
      },
      error => {
        console.log(error);
      }
    );
  }

  private getProcessedImage(id, attempt: number) {
    this.http.get('http://localhost:8080/api/image?id=' + id, {responseType: 'text'}).subscribe(
      data => {
        this.isLoading = false;
        this.imageAsBase64 = 'data:image/jpg;base64,' + data;
      },
      error => {
        if (attempt < 20) {
          setTimeout(() => {
            this.getProcessedImage(id, attempt + 1);
          }, 2000);
        } else {
          this.isLoading = false;
          this.onClose();
          alert('Spróbuj ponownie później');
        }
      }
    );
  }

  public onClose() {
    this.dialogRef.close();
  }

}

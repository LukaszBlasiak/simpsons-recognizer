import { Component } from '@angular/core';
import {FileHolder} from 'angular2-image-upload';
import {MatDialog} from '@angular/material';
import {PreviewDialogComponent} from './preview-dialog/preview-dialog.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  constructor(public dialog: MatDialog) {}

  title = 'simpsons-recognizer';

  onUploadFinished(file: FileHolder) {
    this.dialog.open(PreviewDialogComponent, {
      width: '95%',
      height: '95%',
      maxWidth: '95%',
      data: file.src
    });
  }

}

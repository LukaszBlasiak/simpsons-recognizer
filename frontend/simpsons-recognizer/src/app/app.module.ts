import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule} from '@angular/common/http';
import { ImageUploadModule } from 'angular2-image-upload';
import {MatFileUploadModule} from 'angular-material-fileupload';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatButtonModule} from '@angular/material';
import {MatDialogModule} from '@angular/material/dialog';
import { PreviewDialogComponent } from './preview-dialog/preview-dialog.component';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';

@NgModule({
  declarations: [
    AppComponent,
    PreviewDialogComponent
  ],
  imports: [
    MatButtonModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatFileUploadModule,
    ImageUploadModule.forRoot(),
    BrowserAnimationsModule,
    MatDialogModule,
    MatProgressSpinnerModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents: [
    PreviewDialogComponent
  ]
})
export class AppModule { }
